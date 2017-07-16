from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Role(models.Model):
    """
    Description: Model Description
    """
    role_name = models.CharField(max_length=50)

    class Meta:
        pass

class Angkatan(models.Model):
    """
    Description: Model Description
    """
    year = models.CharField(max_length=10)
    name = models.CharField(max_length=50)

    class Meta:
        pass

class UserProfile(models.Model):
    """
    Description: Model Description
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    npm = models.CharField(max_length=10)
    email = models.CharField(max_length=50)
    role = models.ForeignKey(Role, default=None)
    angkatan = models.ForeignKey(Angkatan)
    photo = models.ImageField(upload_to='uploads/', null=True)
    about = models.TextField(null=True)
    linkedin = models.CharField(max_length=50, null=True)
    facebook = models.CharField(max_length=50, null=True)
    phone_number = models.CharField(max_length=20, null=True)
    birth_place = models.CharField(max_length=50, null=True)
    birth_date = models.DateField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_at']
