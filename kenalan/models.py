from django.db import models
from datetime import timedelta
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

def default_end_time():
    now = timezone.now()
    end_time = now + timedelta(minutes=5)
    return end_time 


class Token(models.Model):
    """
    Description: Model Description
    """
    token = models.CharField(max_length=6, primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_time = models.DateTimeField(auto_now=True)
    end_time = models.DateTimeField(default=default_end_time)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['token']


class KenalanStatus(models.Model):
    """
    Description: Model Description
    """
    status = models.CharField(max_length=50)

    class Meta:
        pass


class Kenalan(models.Model):
    """
    Description: Model Description
    """
    user_elemen = models.ForeignKey(User, related_name='user_elemen')
    user_maba = models.ForeignKey(User, related_name='user_maba')
    status = models.ForeignKey(KenalanStatus, default=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_at']
        unique_together = (("user_elemen", "user_maba"),)


class DetailKenalan(models.Model):
    """
    Description: Model Description
    """
    kenalan = models.ForeignKey(Kenalan, related_name='detail_kenalan')
    name = models.CharField(max_length=50, null=True)
    phone_number = models.CharField(max_length=20, null=True)
    birth_place = models.CharField(max_length=50, null=True)
    birth_date = models.DateField(null=True)
    asal_sma = models.CharField(max_length=50, null=True)
    story = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['updated_at']