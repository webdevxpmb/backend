from rest_framework import permissions
from account.models import UserProfile


ROLE_ELEMEN = 'elemen'
ROLE_AKADEMIS = 'admin'
ROLE_MABA = 'mahasiswa baru'

class IsOwnerOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Instance must have a field named `id`.
        return obj.id == request.user.id


class IsOwner(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        # Instance must have a field named `id`.
        return obj.id == request.user.id


class IsAdmin(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Instance must have a field named `id`.
        return obj.id == request.user.id

class IsElemen(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):

        try:
            user_profile = UserProfile.objects.get(user=request.user)
            role = user_profile.role
            if role.role_name == ROLE_ELEMEN:
                return obj.id == request.user.id
            else:
                return False
        except Exception as e:
            return False

    def has_permission(self, request, view):
        # Instance must have a field named `id`.
        try:
            user_profile = UserProfile.objects.get(user=request.user)
            role = user_profile.role
            if role.role_name == ROLE_ELEMEN:
                return True
            else:
                return False
        except Exception as e:
            return False

