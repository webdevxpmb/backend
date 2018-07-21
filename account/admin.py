from django.contrib import admin
from account.models import (
    Role, Angkatan, UserProfile,
)

from django.contrib.auth.models import User
from django.contrib.auth.models import Group

# Register your models here.


class RoleModelAdmin(admin.ModelAdmin):

    def has_change_permission(self, request, obj=None):
        if request.user.is_superuser == True:
            return True
        return False

    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser == True:
            return True
        return False

    def has_add_permission(self, request):
        if request.user.is_superuser == True:
            return True
        return False

    class Meta:
        model = Role

class AngkatanModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'year')

    def has_change_permission(self, request, obj=None):
        if request.user.is_superuser == True:
            return True
        return False

    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser == True:
            return True
        return False

    def has_add_permission(self, request):
        if request.user.is_superuser == True:
            return True
        return False
    class Meta:
        model = Angkatan


class UserProfileModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'npm', 'angkatan', 'role')
    list_filter = ('angkatan', 'role')
    search_fields = ('name', 'user__username', 'npm')

    def get_readonly_fields(self, request, obj=None):
        if request.user.is_superuser == True:
            return ()
        return ('user', 'name', 'npm', 'angkatan', 'role', 'email',
                       'photo', 'about', 'linkedin', 'facebook', 'phone_number',
                       'birth_place', 'birth_date')

    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser == True:
            return True
        return False

    def has_add_permission(self, request):
        if request.user.is_superuser == True:
            return True
        return False

    class Meta:
        model = UserProfile

admin.site.register(Role, RoleModelAdmin)
admin.site.register(Angkatan, AngkatanModelAdmin)
admin.site.register(UserProfile, UserProfileModelAdmin)
admin.site.unregister(User)
admin.site.unregister(Group)