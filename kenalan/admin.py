from django.contrib import admin

# Register your models here.
from kenalan.models import (
    Kenalan, KenalanStatus, DetailKenalan
)

admin.site.register(Kenalan)
admin.site.register(KenalanStatus)
admin.site.register(DetailKenalan)
