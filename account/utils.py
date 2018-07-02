from django.core.exceptions import PermissionDenied
from django.conf import settings
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView
from account.models import UserProfile
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework_jwt.settings import api_settings
import json
EMAIL_DOMAIN = '@ui.ac.id'
ANGKATAN = {"2017": "2017", "2016": "omega", 
            "2015": "capung", "2014": "orion", 
            "2013--": "alumni"}


def get_angkatan_by_npm(npm):
    try:
        ANGKATAN = load_data(settings.BASE_DIR + "/account/" + 'data_angkatan.json')
        suffix = npm[:2]        # get first two digit of NPM
        angkatan = '20' + suffix
        
        return ANGKATAN[angkatan]

    except Exception as e:
        return ANGKATAN['2013--']


def get_role_by_angkatan(angkatan):
    try:
        ANGKATAN = load_data(settings.BASE_DIR + "/account/" + 'data_angkatan.json')
        if angkatan == ANGKATAN['maba']:
            return "mahasiswa baru"
        else:
            return "elemen"

    except Exception as e:
        return "elemen"


def get_email_by_username(username):
    try:
        return username + EMAIL_DOMAIN
    except Exception as e:
        return username


def load_data(data_dir):
    try:
        with open(data_dir) as data_file:    
            data = json.load(data_file)
        return data
    except Exception as e:
        return {'allowed_org':[]}


@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def configure_token(request):
    try:
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

        payload = jwt_payload_handler(request.user)
        token = jwt_encode_handler(payload)

        data = {'user': request.user.username, 'token': token}
        return Response(data)
    except Exception as e:
        raise PermissionDenied


class SSOAuth(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'index.html'

    def get(self, request):
        try:
            jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
            jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

            payload = jwt_payload_handler(request.user)
            token = jwt_encode_handler(payload)

            user_profile = UserProfile.objects.get(user=request.user)
            profile_id = user_profile.id
            name = user_profile.name
            npm = user_profile.npm
            email = user_profile.email
            role = user_profile.role.role_name
            angkatan = user_profile.angkatan.name

            data = {'user_id': request.user.id, 'user': request.user.username, 'token': token, 'profile_id': profile_id,
                    'name': name, 'npm': npm, 'email': email, 'role': role, 'angkatan': angkatan}
            return Response(data)
        except Exception as e:
            raise

