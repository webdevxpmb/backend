from rest_framework import permissions
from account.models import UserProfile

ROLE_ELEMEN = 'elemen'
ROLE_ADMIN = 'admin'
ROLE_MABA = 'mahasiswa baru'


class IsUserProfileOwner(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        # Instance must have a field named `id`.
        try:
            return obj.user == request.user
        except Exception as e:
            return False


class IsPmbAdmin(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):

        try:
            user_profile = UserProfile.objects.get(user=request.user)
            role = user_profile.role
            if role.role_name == ROLE_ADMIN:
                return True
            else:
                return False
        except Exception as e:
            return False

    def has_permission(self, request, view):
        # Instance must have a field named `id`.
        try:
            user_profile = UserProfile.objects.get(user=request.user)
            role = user_profile.role
            if role.role_name == ROLE_ADMIN:
                return True
            else:
                return False
        except Exception as e:
            return False


class IsElemen(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):

        try:
            user_profile = UserProfile.objects.get(user=request.user)
            role = user_profile.role
            if role.role_name == ROLE_ELEMEN:
                return True
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


class IsMaba(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):

        try:
            user_profile = UserProfile.objects.get(user=request.user)
            role = user_profile.role
            if role.role_name == ROLE_MABA:
                return True
            else:
                return False
        except Exception as e:
            return False

    def has_permission(self, request, view):
        # Instance must have a field named `id`.
        try:
            user_profile = UserProfile.objects.get(user=request.user)
            role = user_profile.role
            if role.role_name == ROLE_MABA:
                return True
            else:
                return False
        except Exception as e:
            return False


class IsDetailKenalanOwner(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        try:
            kenalan = obj.kenalan
            if request.user == kenalan.user_maba or \
                    request.user == kenalan.user_elemen:
                return True
            else:
                return False
        except Exception as e:
            return False

class IsKenalanOwner(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        try:
            if request.user == obj.user_maba or \
                    request.user == obj.user_elemen:
                return True
            else:
                return False
        except Exception as e:
            return False
