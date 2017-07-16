from django.contrib import admin

# Register your models here.
from kenalan.models import (
    Token, Kenalan, KenalanStatus, KenalanDetail
)

admin.site.register(Kenalan)
admin.site.register(KenalanStatus)
admin.site.register(KenalanDetail)
