from rest_framework.pagination import PageNumberPagination
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from website.models import (
    Task, Event, Submission,
    TaskStatistic, UserStatistic,
    )
from kenalan.models import Kenalan
from account.models import UserProfile

ROLE_MABA = "mahasiswa baru"
KENALAN_ACCEPTED = "accepted"
KENALAN_PENDING = "pending"
ANGKATAN_OMEGA = "omega"
ANGKATAN_CAPUNG = "capung"
ANGKATAN_ORION = "orion"
ANGKATAN_ALUMNI = "alumni"


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


@receiver(post_save, sender=Task)
def task_create_or_update(sender, created, instance, **kwargs):
    try:
        if created:
            task = instance
            TaskStatistic.objects.create(task=task, amount=0)
            if instance.is_kenalan:
                user_profile_maba = UserProfile.objects.filter(role__role_name=ROLE_MABA)

                for user_profile in user_profile_maba:
                    user = user_profile.user
                    UserStatistic.objects.create(user=user, task=task, name=task.name + ' statistic',)
        else:
            pass
    except Exception:
        raise


@receiver(post_save, sender=Kenalan)
def kenalan_create_or_update(sender, created, instance, **kwargs):
    try:
        kenalan = instance
        user_maba = kenalan.user_maba
        user_elemen = kenalan.user_elemen
        user_elemen_profile = UserProfile.objects.get(user=user_elemen)
        user_elemen_angkatan = user_elemen_profile.angkatan.name
        user_statistic = UserStatistic.objects.get(user=user_maba)
        if created:
            if user_elemen_angkatan == ANGKATAN_OMEGA:
                user_statistic.amount_omega += 1
            elif user_elemen_angkatan == ANGKATAN_CAPUNG:
                user_statistic.amount_capung += 1
            elif user_elemen_angkatan == ANGKATAN_ORION:
                user_statistic.amount_orion += 1
            elif user_elemen_angkatan == ANGKATAN_ALUMNI:
                user_statistic.amount_alumni += 1
        else:
            if kenalan.status.status == KENALAN_ACCEPTED:
                if user_elemen_angkatan == ANGKATAN_OMEGA:
                    user_statistic.amount_approved_omega += 1
                elif user_elemen_angkatan == ANGKATAN_CAPUNG:
                    user_statistic.amount_approved_capung += 1
                elif user_elemen_angkatan == ANGKATAN_ORION:
                    user_statistic.amount_approved_orion += 1
                elif user_elemen_angkatan == ANGKATAN_ALUMNI:
                    user_statistic.amount_approved_alumni += 1
            else:
                pass
        user_statistic.save()
    except Exception:
        pass
