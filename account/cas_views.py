"""CAS login/logout replacement views"""
from __future__ import absolute_import
from __future__ import unicode_literals
from urlparse import urlunparse # For python 2.7
# from urllib.parse import urlparse # For python 3.4
from account.models import UserProfile
from django.shortcuts import render
from rest_framework_jwt.settings import api_settings
from django.conf import settings
from django.http import HttpResponseRedirect
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import (
    logout as auth_logout,
    login as auth_login,
    authenticate
)
from django.contrib import messages
from django.utils.translation import ugettext_lazy as _
from django.views.decorators.http import require_http_methods

from importlib import import_module

import logging

from datetime import timedelta

from django_cas_ng.signals import cas_user_logout
from django_cas_ng.models import ProxyGrantingTicket, SessionTicket
from django_cas_ng.utils import (get_cas_client, get_service_url,
                    get_protocol, get_redirect_url,
                    get_user_from_session)

SessionStore = import_module(settings.SESSION_ENGINE).SessionStore
__all__ = ['login', 'logout', 'callback']
jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

@csrf_exempt
@require_http_methods(["GET", "POST"])
def login(request, next_page=None, required=False):
    """Forwards to CAS login URL or verifies CAS ticket"""
    service_url = get_service_url(request, next_page)
    client = get_cas_client(service_url=service_url)

    if not next_page and settings.CAS_STORE_NEXT and 'CASNEXT' in request.session:
        next_page = request.session['CASNEXT']
        del request.session['CASNEXT']

    if not next_page:
        next_page = get_redirect_url(request)

    if request.user.is_authenticated():
        if settings.CAS_LOGGED_MSG is not None:
            message = settings.CAS_LOGGED_MSG % request.user.get_username()
            messages.success(request, message)
            user = request.user
            payload = jwt_payload_handler(user)
            token = jwt_encode_handler(payload)
            user_profile = UserProfile.objects.get(user=user)
            profile_id = user_profile.id
            name = user_profile.name
            npm = user_profile.npm
            email = user_profile.email
            role = user_profile.role.role_name
            angkatan = user_profile.angkatan.name

            data = {'user_id': user.id, 'user': user.username, 'token': token,
                    'profile_id': profile_id,
                    'name': name, 'npm': npm, 'email': email, 'role': role, 'angkatan': angkatan}
            return render(request, 'index.html', data)
        return render(request, 'index.html')

    ticket = request.GET.get('ticket')
    if ticket:
        user = authenticate(ticket=ticket,
                            service=service_url,
                            request=request)
        pgtiou = request.session.get("pgtiou")
        if user is not None:
            if not request.session.exists(request.session.session_key):
                request.session.create()
            auth_login(request, user)
            SessionTicket.objects.create(
                session_key=request.session.session_key,
                ticket=ticket
            )
            if pgtiou and settings.CAS_PROXY_CALLBACK:
                # Delete old PGT
                ProxyGrantingTicket.objects.filter(
                    user=user,
                    session_key=request.session.session_key
                ).delete()
                # Set new PGT ticket
                try:
                    pgt = ProxyGrantingTicket.objects.get(pgtiou=pgtiou)
                    pgt.user = user
                    pgt.session_key = request.session.session_key
                    pgt.save()
                except ProxyGrantingTicket.DoesNotExist:
                    pass

            if settings.CAS_LOGIN_MSG is not None:
                name = user.get_username()
                message = settings.CAS_LOGIN_MSG % name
                messages.success(request, message)

            try:
                payload = jwt_payload_handler(user)
                token = jwt_encode_handler(payload)

                user_profile = UserProfile.objects.get(user=user)
                profile_id = user_profile.id
                name = user_profile.name
                npm = user_profile.npm
                email = user_profile.email
                role = user_profile.role.role_name
                angkatan = user_profile.angkatan.name

                data = {'user_id': user.id, 'user': user.username, 'token': token,
                        'profile_id': profile_id,
                        'name': name, 'npm': npm, 'email': email, 'role': role, 'angkatan': angkatan}
                return render(request, 'index.html', data)
            except Exception as e:
                logging.debug(e)
                raise
        elif settings.CAS_RETRY_LOGIN or required:
            return HttpResponseRedirect(client.get_login_url())
        else:
            raise PermissionDenied(_('Login failed.'))
    else:
        return HttpResponseRedirect(client.get_login_url())


@require_http_methods(["GET"])
def logout(request, next_page=None):
    """Redirects to CAS logout page"""
    # try to find the ticket matching current session for logout signal
    sts = SessionTicket.objects.filter(session_key=request.session.session_key)
    # send logout signal
    for st in sts:
        cas_user_logout.send(
            sender="manual",
            user=request.user,
            session=request.session,
            ticket=st.ticket,
        )
    auth_logout(request)
    # clean current session ProxyGrantingTicket and SessionTicket
    ProxyGrantingTicket.objects.filter(session_key=request.session.session_key).delete()
    SessionTicket.objects.filter(session_key=request.session.session_key).delete()
    if settings.CAS_LOGOUT_COMPLETELY:
        client = get_cas_client()

        return HttpResponseRedirect(client.get_logout_url(settings.CLIENT_HOST))
    else:
        # This is in most cases pointless if not CAS_RENEW is set. The user will
        # simply be logged in again on next request requiring authorization.
        return render(request, 'index.html')

@csrf_exempt
@require_http_methods(["GET", "POST"])
def callback(request):
    """Read PGT and PGTIOU sent by CAS"""
    if request.method == 'POST' and request.POST.get('logoutRequest'):
        clean_sessions(get_cas_client(), request)
        return HttpResponse("{0}\n".format(_('ok')), content_type="text/plain")
    elif request.method == 'GET':
        pgtid = request.GET.get('pgtId')
        pgtiou = request.GET.get('pgtIou')
        pgt = ProxyGrantingTicket.objects.create(pgtiou=pgtiou, pgt=pgtid)
        pgt.save()
        ProxyGrantingTicket.objects.filter(
            session_key=None,
            date__lt=(timezone.now() - timedelta(seconds=60))
        ).delete()
        return HttpResponse("{0}\n".format(_('ok')), content_type="text/plain")


def clean_sessions(client, request):
    for slo in client.get_saml_slos(request.POST.get('logoutRequest')):
        try:
            st = SessionTicket.objects.get(ticket=slo.text)
            session = SessionStore(session_key=st.session_key)
            # send logout signal
            cas_user_logout.send(
                sender="slo",
                user=get_user_from_session(session),
                session=session,
                ticket=slo.text,
            )
            session.flush()
            # clean logout session ProxyGrantingTicket and SessionTicket
            ProxyGrantingTicket.objects.filter(session_key=st.session_key).delete()
            SessionTicket.objects.filter(session_key=st.session_key).delete()
        except SessionTicket.DoesNotExist:
            pass
