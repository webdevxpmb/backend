from django.contrib import admin

# Register your models here.
from kenalan.models import (
    Kenalan, KenalanStatus, DetailKenalan, Token,
)
from django.utils.translation import ugettext_lazy as _

ADMIN_PMB = 'adminpmb'
SUPER_ADMIN = 'admin'


from django.utils.translation import ugettext_lazy as _


class KenalanListFilter(admin.SimpleListFilter):
    # Human-readable title which will be displayed in the
    # right admin sidebar just above the filter options.
    title = _('Angkatan Elemen')

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
    list_filter = (KenalanListFilter, 'status', )

    def get_readonly_fields(self, request, obj=None):
        if request.user.username == ADMIN_PMB or request.user.username == SUPER_ADMIN:
            return ()
        return ('user_maba', 'user_elemen',)

    def has_delete_permission(self, request, obj=None):
        if request.user.username == ADMIN_PMB or request.user.username == SUPER_ADMIN:
            return True
        return False

    def has_add_permission(self, request):
        if request.user.username == ADMIN_PMB or request.user.username == SUPER_ADMIN:
            return True
        return False

    class Meta:
        model = Kenalan


class KenalanStatusModelAdmin(admin.ModelAdmin):
    def has_change_permission(self, request, obj=None):
        if request.user.username == ADMIN_PMB or request.user.username == SUPER_ADMIN:
            return True
        return False

    def has_delete_permission(self, request, obj=None):
        if request.user.username == ADMIN_PMB or request.user.username == SUPER_ADMIN:
            return True
        return False

    def has_add_permission(self, request):
        if request.user.username == ADMIN_PMB or request.user.username == SUPER_ADMIN:
            return True
        return False

    class Meta:
        model = KenalanStatus


class DetailKenalanListFilter(admin.SimpleListFilter):
    # Human-readable title which will be displayed in the
    # right admin sidebar just above the filter options.
    title = _('Angkatan Elemen')

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
            return queryset.filter(kenalan__user_elemen__profile__angkatan__name='omega')
        if self.value() == '2015':
            return queryset.filter(kenalan__user_elemen__profile__angkatan__name='capung')
        if self.value() == '2014':
            return queryset.filter(kenalan__user_elemen__profile__angkatan__name='orion')
        if self.value() == '2013--':
            return queryset.filter(kenalan__user_elemen__profile__angkatan__name='alumni')


class DetailKenalanModelAdmin(admin.ModelAdmin):
    list_display = ('user_maba', 'user_elemen', 'angkatan_elemen', 'kenalan')
    list_filter = (DetailKenalanListFilter,)
    search_fields = ('kenalan__user_maba__profile__name', 'kenalan__user_elemen__profile__name')

    def user_maba(self, obj):
        return obj.kenalan.user_maba

    def user_elemen(self, obj):
        return obj.kenalan.user_elemen

    def angkatan_elemen(self, obj):
        return obj.kenalan.user_elemen.profile.angkatan

    def get_readonly_fields(self, request, obj=None):
        if request.user.username == ADMIN_PMB or request.user.username == SUPER_ADMIN:
            return ()
        return ('name', 'phone_number', 'birth_place', 'birth_date', 'asal_sma', 'story',)

    def has_delete_permission(self, request, obj=None):
        if request.user.username == ADMIN_PMB or request.user.username == SUPER_ADMIN:
            return True
        return False

    def has_add_permission(self, request):
        if request.user.username == ADMIN_PMB or request.user.username == SUPER_ADMIN:
            return True
        return False

    class Meta:
        model = DetailKenalan


class TokenModelAdmin(admin.ModelAdmin):
    def has_change_permission(self, request, obj=None):
        if request.user.username == ADMIN_PMB or request.user.username == SUPER_ADMIN:
            return True
        return False

    def has_delete_permission(self, request, obj=None):
        if request.user.username == ADMIN_PMB or request.user.username == SUPER_ADMIN:
            return True
        return False

    def has_add_permission(self, request):
        if request.user.username == ADMIN_PMB or request.user.username == SUPER_ADMIN:
            return True
        return False

    class Meta:
        model = DetailKenalan


admin.site.register(Kenalan, KenalanModelAdmin)
admin.site.register(KenalanStatus, KenalanStatusModelAdmin)
admin.site.register(DetailKenalan, DetailKenalanModelAdmin)
admin.site.register(Token, TokenModelAdmin)