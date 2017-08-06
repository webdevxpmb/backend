from django.contrib import admin

# Register your models here.
from kenalan.models import (
    Kenalan, KenalanStatus, DetailKenalan,
)
from account.models import UserProfile

from django.utils.translation import ugettext_lazy as _


class KenalanListFilter(admin.SimpleListFilter):
    # Human-readable title which will be displayed in the
    # right admin sidebar just above the filter options.
    title = _('Angkatan')

    # Parameter for the filter that will be used in the URL query.
    parameter_name = 'angkatan'

    def lookups(self, request, model_admin):
        """
        Returns a list of tuples. The first element in each
        tuple is the coded value for the option that will
        appear in the URL query. The second element is the
        human-readable name for the option that will appear
        in the right sidebar.
        """
        return (
            ('2016', _('omega')),
            ('2015', _('capung')),
            ('2014', _('orion')),
            ('2013--', _('alumni'))
        )

    def queryset(self, request, queryset):
        """
        Returns the filtered queryset based on the value
        provided in the query string and retrievable via
        `self.value()`.
        """
        # Compare the requested value (either '80s' or '90s')
        # to decide how to filter the queryset.
        if self.value() == '2016':
            return queryset.filter(user_elemen__profile__angkatan__name='omega')
        if self.value() == '2015':
            return queryset.filter(user_elemen__profile__angkatan__name='capung')
        if self.value() == '2014':
            return queryset.filter(user_elemen__profile__angkatan__name='orion')
        if self.value() == '2013--':
            return queryset.filter(user_elemen__profile__angkatan__name='alumni')


class KenalanModelAdmin(admin.ModelAdmin):
    list_display = ('user_maba', 'user_elemen', 'status', 'updated_at')
    list_filter = (KenalanListFilter, )

    class Meta:
        model = Kenalan

admin.site.register(Kenalan, KenalanModelAdmin)
admin.site.register(KenalanStatus)
admin.site.register(DetailKenalan)
