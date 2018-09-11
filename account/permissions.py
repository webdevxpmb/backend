import logging
from rest_framework import permissions
from account.models import UserProfile

ROLE_ELEMEN = 'elemen'
ROLE_ADMIN = 'admin'
ROLE_MABA = 'mahasiswa baru'


def is_maba(user):
    try:
        user_profile = UserProfile.objects.get(user=user)
        role = user_profile.role
        if role.role_name == ROLE_MABA:
            return True
        else:
            return False
    except Exception as e:
        return False


def is_elemen(user):
    try:
        user_profile = UserProfile.objects.get(user=user)
        role = user_profile.role
        if role.role_name == ROLE_ELEMEN:
            return True
        else:
            return False
    except Exception as e:
        return False


def is_pmb_admin(user):
    try:
        user_profile = UserProfile.objects.get(user=user)
        role = user_profile.role
        if role.role_name == ROLE_ADMIN:
            return True
        else:
            return False
    except Exception as e:
        return False


class IsOwner(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        # Instance must have a field named `id`.
        try:
            if hasattr(obj, 'user'):
                return obj.user == request.user
            elif hasattr(obj, 'author_id'):
                return obj.author_id == request.user.id

        except Exception as e:
            raise


class IsPmbAdmin(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return is_pmb_admin(request.user)

    def has_permission(self, request, view):
        return is_pmb_admin(request.user)


class IsElemen(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return is_elemen(request.user)

    def has_permission(self, request, view):
        return is_elemen(request.user)


class IsMaba(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return is_maba(request.user)

    def has_permission(self, request, view):
        return is_maba(request.user)


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
                logging.debug(user)
                return False
        except Exception as e:
            logging.debug(e)
            return False


class IsMabaOrElemen(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return is_maba(request.user) or is_elemen(request.user)

    def has_permission(self, request, view):
        return is_maba(request.user) or is_elemen(request.user)


class IsMabaOrAdmin(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return is_maba(request.user) or is_pmb_admin(request.user)

    def has_permission(self, request, view):
        return is_maba(request.user) or is_pmb_admin(request.user)


class IsElemenOrAdmin(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return is_elemen(request.user) or is_pmb_admin(request.user)

    def has_permission(self, request, view):
        return is_elemen(request.user) or is_pmb_admin(request.user)