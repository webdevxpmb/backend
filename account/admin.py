from django.contrib import admin
from account.models import (
    Role, Angkatan, UserProfile,
)


# Register your models here.


class AngkatanModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'year')

    class Meta:
        model = Angkatan


class UserProfileModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'npm', 'angkatan', 'role')
    readonly_fields = ('name', 'npm')
    list_filter = ('angkatan', 'role')
    search_fields = ('name', 'user__username', 'npm')

    class Meta:
        model = UserProfile

admin.site.register(Role)
admin.site.register(Angkatan, AngkatanModelAdmin)
admin.site.register(UserProfile, UserProfileModelAdmin)
