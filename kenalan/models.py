from django.db import models
from datetime import timedelta
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

def default_end_time():
    now = timezone.now()
    end_time = now + timedelta(minutes=1)
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


class Kenalan(models.Model):
    """
    Description: Model Description
    """
    user1 = models.ForeignKey(User, related_name='user1')
    user2 = models.ForeignKey(User, related_name='user2')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_at']


class KenalanStatus(models.Model):
    """
    Description: Model Description
    """
    status = models.CharField(max_length=50)

    class Meta:
        pass

class KenalanDetail(models.Model):
    """
    Description: Model Description
    """
    kenalan = models.ForeignKey(Kenalan)
    status = models.ForeignKey(KenalanStatus)
    name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=20)
    birth_place = models.CharField(max_length=50, null=True)
    birth_date = models.DateField(null=True)
    asal_sma = models.CharField(max_length=50)
    story = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['updated_at']