from django.contrib.auth.models import User

from account.models import (
    Role, Angkatan, UserProfile,
)

from account.serializers import( 
    UserSerializer, RoleSerializer,
    AngkatanSerializer, UserProfileSerializer,
)
from rest_framework import generics, permissions
from account.permissions import(
    IsUserProfileOwner,
    IsPmbAdmin,
)

# Create your views here.


class UserList(generics.ListAPIView):
    permission_classes = (permissions.IsAdminUser,)
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAdminUser,)
    queryset = User.objects.all()
    serializer_class = UserSerializer


class RoleList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAdminUser,)
    queryset = Role.objects.all()
    serializer_class = RoleSerializer


class RoleDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAdminUser,)
    queryset = Role.objects.all()
    serializer_class = RoleSerializer


class AngkatanList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAdminUser,)
    queryset = Angkatan.objects.all()
    serializer_class = AngkatanSerializer


class AngkatanDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAdminUser,)
    queryset = Angkatan.objects.all()
    serializer_class = AngkatanSerializer


class UserProfileList(generics.ListCreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    search_fields = ('name', 'npm')


class UserProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = (IsUserProfileOwner,)
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
