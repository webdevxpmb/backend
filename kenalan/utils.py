from account.permissions import IsElemen
from kenalan.models import Token, Kenalan, KenalanDetail, KenalanStatus
from kenalan.serializers import TokenSerializer, KenalanSerializer
from account.models import UserProfile
from django.utils.crypto import get_random_string

from rest_framework.exceptions import APIException, PermissionDenied
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes

import json
import datetime


@api_view(['GET'])
# @permission_classes((IsElemen, ))
def generate_token(request):
    try:
        user = request.user
        if not check_user(user):
            token = get_token()

            content = Token.objects.create(token=token, user=user)
            content = TokenSerializer(content, context={'request': request})

            return Response(content.data)

        else:
            content = Token.objects.get(user=user)
            content = TokenSerializer(content, context={'request': request})

            return Response(content.data, status=200)
    except Exception as e:
        raise Response(status=400)


def get_token():
    token = get_random_string(length=6, allowed_chars='1234567890')
    if check_token(token):
        return token    
    else:
        return get_token()


def check_token(token):
    try:
        token_count = Token.objects.filter(token=token).count()
        return token_count == 0
    except Exception as e:
        raise APIException

def check_user(user):
    try:
        token_count = Token.objects.filter(user=user).count()
        return token_count >= 1
    except Exception as e:
        raise APIException

@api_view(['GET'])
@permission_classes((IsElemen, ))
def delete_expired_token(request):
    try:
        now = datetime.datetime.now().replace(tzinfo=None)
        expired_token = Token.objects.filter(user=request.user ,end_time__lt=now)
        expired_token.delete()
        return Response(status=200)
    except Exception as e:
        return Response(status=501)

def delete_all_expired_token():
    try:
        now = datetime.datetime.now().replace(tzinfo=None)
        expired_token = Token.objects.filter(end_time__lt=now)
        expired_token.delete()
    except Exception as e:
        pass

@api_view(['GET'])
def create_kenalan_by_token(request, token):
    try:
        if not check_token(token):
            token = Token.objects.get(token=token)
            user_elemen = token.user
            user_maba = request.user
            elemen_profile = UserProfile.objects.get(user=user_elemen)

            kenalan = Kenalan.objects.create(user_elemen=user_elemen, user_maba=user_maba)
            # create initial detail
            kenalan_status = KenalanStatus.objects.get(id=2)
            kenalan_detail = KenalanDetail.objects.create(kenalan=kenalan,
                                                          status=kenalan_status,
                                                          name=elemen_profile.name)

            content = KenalanSerializer(kenalan, context={'request': request})
            return Response(content.data, status=200)
            
        else:
            return Response({'data': 'invalid token'})

    except Exception as e:
        raise