from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Role(models.Model):
    """
    Description: Model Description
    """
    role_name = models.CharField(max_length=50)

    def __str__(self):
        return self.role_name

    class Meta:
        pass


class Angkatan(models.Model):
    """
    Description: Model Description
    """
    year = models.CharField(max_length=50)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        pass


class UserProfile(models.Model):
    """
    Description: Model Description
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    name = models.CharField(max_length=128)
    npm = models.CharField(max_length=10)
    email = models.CharField(max_length=128)
    role = models.ForeignKey(Role)
    angkatan = models.ForeignKey(Angkatan)
    photo = models.ImageField(upload_to='images/', blank=True, null=True)
    about = models.TextField(blank=True, null=True)
    asal_sekolah = models.CharField(max_length=100, null=True)
    link_gdrive = models.CharField(max_length=100, null=True)
    line_id = models.CharField(max_length=100, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    birth_place = models.CharField(max_length=100, blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    score = models.FloatField(blank=True, null=True, default=0.0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['created_at']
