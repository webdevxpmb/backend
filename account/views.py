from django.contrib.auth.models import User
from rest_framework.parsers import FileUploadParser, JSONParser
from account.models import (
    Role, Angkatan, UserProfile,
)

from account.serializers import( 
    UserSerializer, RoleSerializer,
    AngkatanSerializer, UserProfileSerializer,
)
from rest_framework import generics
from account.permissions import(
    IsOwner,
    IsPmbAdmin,
)


class UserList(generics.ListAPIView):
    permission_classes = (IsPmbAdmin,)
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsPmbAdmin,)
    queryset = User.objects.all()
    serializer_class = UserSerializer


class RoleList(generics.ListCreateAPIView):
    permission_classes = (IsPmbAdmin,)
    queryset = Role.objects.all()
    serializer_class = RoleSerializer


class RoleDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsPmbAdmin,)
    queryset = Role.objects.all()
    serializer_class = RoleSerializer


class AngkatanList(generics.ListCreateAPIView):
    permission_classes = (IsPmbAdmin,)
    queryset = Angkatan.objects.all()
    serializer_class = AngkatanSerializer


class AngkatanDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsPmbAdmin,)
    queryset = Angkatan.objects.all()
    serializer_class = AngkatanSerializer


class UserProfileList(generics.ListAPIView):
    permission_classes = (IsPmbAdmin,)
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    filter_fields = ('role', 'angkatan')


class UserProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwner,)
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    parser_classes = (JSONParser, FileUploadParser, )
