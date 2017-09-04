from rest_framework.pagination import PageNumberPagination
from django.db.models.signals import post_save
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser
from django.dispatch import receiver
from rest_framework.response import Response

from website.models import (
    Task, Submission,
    TaskStatistic, UserStatistic,
    )
from kenalan.models import Kenalan
from account.models import UserProfile
import datetime

import datetime

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
                    UserStatistic.objects.create(user=user, task=task, name=task.name + ' statistic')
        else:
            pass
    except Exception:
        raise


@receiver(post_save, sender=Kenalan)
def kenalan_create_or_update(sender, created, instance, **kwargs):
    try:
        user_maba = instance.user_maba
        user_statistic = UserStatistic.objects.get(user=user_maba)
        task = user_statistic.task
        now = datetime.datetime.now().replace(tzinfo=None)
        if task.end_time >= now:
            user_statistic.amount_omega = Kenalan.objects.filter(user_maba=user_maba,
                                                                 user_elemen__profile__angkatan__name='omega').count()
            user_statistic.amount_capung = Kenalan.objects.filter(user_maba=user_maba,
                                                                  user_elemen__profile__angkatan__name='capung').count()
            user_statistic.amount_orion = Kenalan.objects.filter(user_maba=user_maba,
                                                                 user_elemen__profile__angkatan__name='orion').count()
            user_statistic.amount_alumni = Kenalan.objects.filter(user_maba=user_maba,
                                                                  user_elemen__profile__angkatan__name='alumni').count()


        user_statistic.amount_approved_omega = Kenalan.objects.filter(user_maba=user_maba,
                                                                      user_elemen__profile__angkatan__name='omega',
                                                                      status__status='approved',
                                                                      created_at__gt=task.start_time,
                                                                      created_at__lt=task.end_time).count()
        user_statistic.amount_approved_capung = Kenalan.objects.filter(user_maba=user_maba,
                                                                       user_elemen__profile__angkatan__name='capung',
                                                                       status__status='approved',
                                                                       created_at__gt=task.start_time,
                                                                       created_at__lt=task.end_time).count()
        user_statistic.amount_approved_orion = Kenalan.objects.filter(user_maba=user_maba,
                                                                      user_elemen__profile__angkatan__name='orion',
                                                                      status__status='approved',
                                                                      created_at__gt=task.start_time,
                                                                      created_at__lt=task.end_time).count()
        user_statistic.amount_approved_alumni = Kenalan.objects.filter(user_maba=user_maba,
                                                                       user_elemen__profile__angkatan__name='alumni',
                                                                       status__status='approved',
                                                                       created_at__gt=task.start_time,
                                                                       created_at__lt=task.end_time).count()
        user_statistic.save()
    except Exception:
        pass


@api_view(['GET'])
@permission_classes((IsAdminUser,))
def update_user_statistic(request):
    user_statistics = UserStatistic.objects.all()

    for user_statistic in user_statistics:
        user_statistic.amount_omega = Kenalan.objects.filter(user_maba=user_statistic.user,
                                              user_elemen__profile__angkatan__name='omega').count()
        user_statistic.amount_capung = Kenalan.objects.filter(user_maba=user_statistic.user,
                                               user_elemen__profile__angkatan__name='capung').count()
        user_statistic.amount_orion = Kenalan.objects.filter(user_maba=user_statistic.user,
                                              user_elemen__profile__angkatan__name='orion').count()
        user_statistic.amount_alumni = Kenalan.objects.filter(user_maba=user_statistic.user,
                                               user_elemen__profile__angkatan__name='alumni').count()

        user_statistic.amount_approved_omega = Kenalan.objects.filter(user_maba=user_statistic.user,
                                                       user_elemen__profile__angkatan__name='omega',
                                                       status__status='accepted').count()
        user_statistic.amount_approved_capung = Kenalan.objects.filter(user_maba=user_statistic.user,
                                                       user_elemen__profile__angkatan__name='capung',
                                                       status__status='accepted').count()
        user_statistic.amount_approved_orion = Kenalan.objects.filter(user_maba=user_statistic.user,
                                                       user_elemen__profile__angkatan__name='orion',
                                                       status__status='accepted').count()
        user_statistic.amount_approved_alumni = Kenalan.objects.filter(user_maba=user_statistic.user,
                                                       user_elemen__profile__angkatan__name='alumni',
                                                       status__status='accepted').count()
        user_statistic.save()

    return Response({'message': 'updated'})


@api_view(['GET'])
def get_server_time(request):
    now = datetime.datetime.now()
    return Response({'server_time': now})
