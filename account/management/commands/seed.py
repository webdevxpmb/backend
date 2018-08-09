from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from account.models import Role, Angkatan
from account.utils import load_data

class Command(BaseCommand):
    help = 'Seed Role and Angkatan from data_angkatan.json'

    def handle(self, *args, **options):
        Role.objects.get_or_create(role_name='admin')
        Role.objects.get_or_create(role_name='elemen')
        Role.objects.get_or_create(role_name='mahasiswa baru')

        data_angkatan = load_data(settings.BASE_DIR + "/account/" + 'data_angkatan.json')
        for tahun, nama in data_angkatan.iteritems():
            if tahun != 'maba':
                angkatan, created = Angkatan.objects.get_or_create(year=tahun)
                angkatan.name = nama
                angkatan.save()
            