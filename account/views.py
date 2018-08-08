from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework.parsers import FileUploadParser, JSONParser
from rest_framework.response import Response
from account.models import (
    Role, Angkatan, UserProfile,
)

from account.serializers import( 
    UserSerializer, RoleSerializer,
    AngkatanSerializer, UserProfileSerializer,
    GetUserProfileSerializer,
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
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = UserProfileSerializer

    def get_queryset(self):
        queryset = UserProfile.objects.filter(user=self.request.user)
        return queryset


class UserProfileDetail(generics.RetrieveUpdateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = GetUserProfileSerializer(instance)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        try:
            print('masuk sini 1')
            self.permission_classes = (IsOwner, )
            print('masuk sini 2')
            partial = kwargs.pop('partial', False)
            print('masuk sini 3')
            instance = self.get_object()
            print('masuk sini 4')
            serializer = self.get_serializer(instance, data=request.data, partial=partial)
            print('masuk sini 5')
            serializer.is_valid(raise_exception=True)
            print('masuk sini 6')
            self.perform_update(serializer)
            print('masuk sini 7')
        except Exception as e:
            print(e)
        return Response(GetUserProfileSerializer(instance).data)

    def delete(self, request, *args, **kwargs):
        self.permission_classes = (IsOwner, )
        return self.destroy(request, *args, **kwargs)