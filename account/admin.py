from django.contrib import admin
from account.models import (
    Role, Angkatan, UserProfile,
)

# Register your models here.

admin.site.register(Role)
admin.site.register(Angkatan)
admin.site.register(UserProfile)
