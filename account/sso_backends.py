
import logging
from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured, PermissionDenied
from rest_framework_jwt.settings import api_settings

from django_cas_ng.signals import cas_user_authenticated
from django_cas_ng.utils import get_cas_client

from account.models import UserProfile, Role, Angkatan
from account.utils import(
    get_angkatan_by_npm,
    get_role_by_angkatan,
    get_email_by_username,
    load_data
    )

__all__ = ['CASBackend']


class CASBackend(ModelBackend):
    """CAS authentication backend"""

    def authenticate(self, request, ticket, service):
        try:
            """Verifies CAS ticket and gets or creates User object"""
            client = get_cas_client(service_url=service)
            username, attributes, pgtiou = client.verify_ticket(ticket)
            if attributes and request:
                request.session['attributes'] = attributes

            if not username:
                return None
            user = None
            username = self.clean_username(username)

            UserModel = get_user_model()
            allowed_org = load_data(settings.BASE_DIR + "/account/" + 'data.json')

            if attributes['kd_org'] not in allowed_org['allowed_org']:
                return None
            # Note that this could be accomplished in one try-except clause, but
            # instead we use get_or_create when creating unknown users since it has
            # built-in safeguards for multiple threads.
            if settings.CAS_CREATE_USER:
                user, created = UserModel._default_manager.get_or_create(**{
                    UserModel.USERNAME_FIELD: username
                })
                if created:
                    user = self.configure_user(user)
                if settings.CAS_APPLY_ATTRIBUTES_TO_USER and attributes:
                    self.configure_user_profile(user, attributes)
            else:
                created = False
                try:
                    user = UserModel._default_manager.get_by_natural_key(username)
                except UserModel.DoesNotExist:
                    pass

            if not self.user_can_authenticate(user):
                return None

            if pgtiou and settings.CAS_PROXY_CALLBACK and request:
                request.session['pgtiou'] = pgtiou

            
                # If we are receiving None for any values which cannot be NULL
                # in the User model, set them to an empty string instead.
                # Possibly it would be desirable to let these throw an error
                # and push the responsibility to the CAS provider or remove
                # them from the dictionary entirely instead. Handling these
                # is a little ambiguous.

            # send the `cas_user_authenticated` signal
            cas_user_authenticated.send(
                sender=self,
                user=user,
                created=created,
                attributes=attributes,
                ticket=ticket,
                service=service,
                request=request
            )
            return user
        except Exception as e:
            logging.debug(e)
            return None

    # ModelBackend has a `user_can_authenticate` method starting from Django
    # 1.10, that only allows active user to log in. For consistency,
    # django-cas-ng will have the same behavior as Django's ModelBackend.
    if not hasattr(ModelBackend, 'user_can_authenticate'):
        def user_can_authenticate(self, user):
            return True

    def clean_username(self, username):
        """
        Performs any cleaning on the "username" prior to using it to get or
        create the user object.  Returns the cleaned username.
        By default, changes the username case according to
        `settings.CAS_FORCE_CHANGE_USERNAME_CASE`.
        """
        username_case = settings.CAS_FORCE_CHANGE_USERNAME_CASE
        if username_case == 'lower':
            username = username.lower()
        elif username_case == 'upper':
            username = username.upper()
        elif username_case is not None:
            raise ImproperlyConfigured(
                "Invalid value for the CAS_FORCE_CHANGE_USERNAME_CASE setting. "
                "Valid values are `'lower'`, `'upper'`, and `None`.")
        return username

    def configure_user(self, user):
        """
        Configures a user after creation and returns the updated user.
        By default, returns the user unmodified.
        """
        return user

    def configure_user_profile(self, user, attributes):
        try:
            if attributes['peran_user'] == 'mahasiswa':
                name = attributes['nama']
                npm = attributes['npm']
                email = get_email_by_username(user.get_username())
                angkatan = Angkatan.objects.get(name=get_angkatan_by_npm(npm))
                role = Role.objects.get(role_name=get_role_by_angkatan(angkatan.name))

            elif attributes['peran_user'] == 'staff':
                name = attributes['nama']
                npm = attributes['nip']
                email = get_email_by_username(user.get_username())
                angkatan = Angkatan.objects.get(name='alumni')
                role = Role.objects.get(role_name=get_role_by_angkatan(angkatan.name))

            if not UserProfile.objects.filter(user=user).exists():
                UserProfile.objects.create(user=user,
                                            name=name,
                                            npm=npm,
                                            email=email,
                                            angkatan=angkatan,
                                            role=role,
                                            )
        except Exception as e:
            logging.debug(e)
            raise PermissionDenied



