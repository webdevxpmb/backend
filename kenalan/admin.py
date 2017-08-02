from django.contrib import admin

# Register your models here.
from kenalan.models import (
    Kenalan, KenalanStatus, DetailKenalan,
)
from account.models import UserProfile

class KenalanModelAdmin(admin.ModelAdmin):
    list_display = ('user_maba', 'user_elemen', 'status', 'updated_at')

    class Meta:
        model = Kenalan

admin.site.register(Kenalan, KenalanModelAdmin)
admin.site.register(KenalanStatus)
admin.site.register(DetailKenalan)
