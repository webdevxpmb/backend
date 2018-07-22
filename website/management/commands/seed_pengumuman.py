from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from website.models import PostType

class Command(BaseCommand):
    help = 'Seed Pengumuman dan Post Biasa'

    def handle(self, *args, **options):
        PostType.objects.get_or_create(post_type='pengumuman')
        PostType.objects.get_or_create(post_type='post biasa')
            