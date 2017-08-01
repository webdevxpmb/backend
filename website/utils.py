from rest_framework.pagination import PageNumberPagination
from django.db.models.signals import post_save
from django.dispatch import receiver
from website.models import Task, Event, Submission
from kenalan.models import Kenalan


@receiver(post_save, sender=Task)
def my_handler(sender, **kwargs):
    pass


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100
