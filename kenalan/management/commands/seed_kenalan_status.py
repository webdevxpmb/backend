from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from kenalan.models import KenalanStatus

class Command(BaseCommand):
    help = 'Seed Kenalan Status'

    def handle(self, *args, **options):
        accepted = KenalanStatus()
        accepted.id = 1
        accepted.status = 'accepted'
        accepted.save()

        pending = KenalanStatus()
        pending.id = 2
        pending.status = 'pending'
        pending.save()

        rejected = KenalanStatus()
        rejected.id = 3
        rejected.status = 'rejected'
        rejected.save()
        
            