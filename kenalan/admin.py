from django.contrib import admin

# Register your models here.
from kenalan.models import (
    Kenalan, KenalanStatus, DetailKenalan, Token,
)

from account.models import Angkatan

from django.utils.translation import ugettext_lazy as _

from account.utils import load_data
from django.conf import settings

# data_angkatan.json harus berisi hanya 6 elemen,
# dimana 2 define maba, 1 define alumni, dan 3 define angkatan aktif
lookup_data = []

def fill_lookup_data():
    daftar_angkatan = load_data(settings.BASE_DIR + "/account/" + 'data_angkatan.json')
    tahun_pmb = int(daftar_angkatan['maba'])
    for year, name in daftar_angkatan.items():
        if ((year.isdigit() and name.isdigit() == False)
            or ('--' in year)):
            lookup_data.append((year, name))

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
        if not lookup_data:
            fill_lookup_data()
        return (
            (lookup_data[0][0], _(lookup_data[0][1])),
            (lookup_data[1][0], _(lookup_data[1][1])),
            (lookup_data[2][0], _(lookup_data[2][1])),
            (lookup_data[3][0], _(lookup_data[3][1]))
        )

    def queryset(self, request, queryset):
        """
        Returns the filtered queryset based on the value
        provide qd in the query string and retrievable via
        `self.value()`.
        """
        # Compare the requested value (either '80s' or '90s')
        # to decide how to filter the queryset.
        if not lookup_data:
            fill_lookup_data()
        if self.value() == lookup_data[0][0]:
            return queryset.filter(user_elemen__profile__angkatan__name=lookup_data[0][1])
        if self.value() == lookup_data[1][0]:
            return queryset.filter(user_elemen__profile__angkatan__name=lookup_data[1][1])
        if self.value() == lookup_data[2][0]:
            return queryset.filter(user_elemen__profile__angkatan__name=lookup_data[2][1])
        if self.value() == lookup_data[3][0]:
            return queryset.filter(user_elemen__profile__angkatan__name=lookup_data[3][1])


class DetailKenalanInline(admin.StackedInline):
    model = DetailKenalan

    def get_readonly_fields(self, request, obj=None):
        if request.user.is_superuser == True:
            return ()
        return ('name', 'phone_number', 'birth_place', 'birth_date', 'asal_sma', 'story',)

    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser == True:
            return True
        return False

    def has_add_permission(self, request):
        if request.user.is_superuser == True:
            return True
        return False

class KenalanModelAdmin(admin.ModelAdmin):
    list_display = ('profile_maba', 'profile_elemen', 'status', 'created_at', 'updated_at', 'story',)
    list_editable = ('status',)
    list_filter = (KenalanListFilter, 'status', )
    search_fields = ('user_maba__profile__name', 'user_elemen__profile__name')
    inlines = [
        DetailKenalanInline,
    ]

    def profile_maba(self, obj):
        return obj.user_maba.profile.name

    def profile_elemen(self, obj):
        if (obj.user_elemen):
            return obj.user_elemen.profile.name
        else:
            return 'alumni'

    def story(self, obj):
        return obj.detail_kenalan.story


    def get_readonly_fields(self, request, obj=None):
        if request.user.is_superuser == True:
            return ()
        return ('user_maba', 'user_elemen',)

    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser == True:
            return True
        return False

    def has_add_permission(self, request):
        if request.user.is_superuser == True:
            return True
        return False

    class Meta:
        model = Kenalan


class KenalanStatusModelAdmin(admin.ModelAdmin):
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
        if not lookup_data:
            fill_lookup_data()
        return (
            (lookup_data[0][0], _(lookup_data[0][1])),
            (lookup_data[1][0], _(lookup_data[1][1])),
            (lookup_data[2][0], _(lookup_data[2][1])),
            (lookup_data[3][0], _(lookup_data[3][1]))
        )

    def queryset(self, request, queryset):
        """
        Returns the filtered queryset based on the value
        provided in the query string and retrievable via
        `self.value()`.
        """
        # Compare the requested value (either '80s' or '90s')
        # to decide how to filter the queryset.
        if not lookup_data:
            fill_lookup_data()
        if self.value() == lookup_data[0][0]:
            return queryset.filter(kenalan__user_elemen__profile__angkatan__name=lookup_data[0][1])
        if self.value() == lookup_data[1][0]:
            return queryset.filter(kenalan__user_elemen__profile__angkatan__name=lookup_data[1][1])
        if self.value() == lookup_data[2][0]:
            return queryset.filter(kenalan__user_elemen__profile__angkatan__name=lookup_data[2][1])
        if self.value() == lookup_data[3][0]:
            return queryset.filter(kenalan__user_elemen__profile__angkatan__name=lookup_data[3][1])


class DetailKenalanModelAdmin(admin.ModelAdmin):
    list_display = ('user_maba', 'user_elemen', 'angkatan_elemen', 'kenalan')
    list_filter = (DetailKenalanListFilter,)
    search_fields = ('kenalan__user_maba__profile__name', 'kenalan__user_elemen__profile__name')

    def user_maba(self, obj):
        return obj.kenalan.user_maba.profile.name

    def user_elemen(self, obj):
        if (obj.kenalan.user_elemen):
            return obj.kenalan.user_elemen.profile.name
        return 'alumni'

    def angkatan_elemen(self, obj):
        if (obj.kenalan.user_elemen):
            return obj.kenalan.user_elemen.profile.angkatan
        return 'alumni'

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
        model = DetailKenalan


class TokenModelAdmin(admin.ModelAdmin):
    list_display = ('user', 'end_time',)


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
        model = DetailKenalan


admin.site.register(Kenalan, KenalanModelAdmin)
admin.site.register(KenalanStatus, KenalanStatusModelAdmin)
admin.site.register(DetailKenalan, DetailKenalanModelAdmin)
admin.site.register(Token, TokenModelAdmin)
