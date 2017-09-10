from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from io import BytesIO
from django.core.files.base import ContentFile
from resizeimage import resizeimage
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
    name = models.CharField(max_length=100)
    npm = models.CharField(max_length=10)
    email = models.CharField(max_length=50)
    role = models.ForeignKey(Role)
    angkatan = models.ForeignKey(Angkatan)
    photo = models.ImageField(upload_to='images/', blank=True, null=True)
    about = models.TextField(blank=True, null=True)
    linkedin = models.CharField(max_length=50, blank=True, null=True)
    facebook = models.CharField(max_length=50, blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    birth_place = models.CharField(max_length=50, blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.photo:
            pil_image_obj = Image.open(self.photo)
            if self.photo.width > 500:
                new_image = resizeimage.resize_width(pil_image_obj, 500)
            else:
                new_image = pil_image_obj

            new_image_io = BytesIO()
            new_image.save(new_image_io, format='JPEG')

            temp_name = self.photo.name
            self.photo.delete(save=False)

            self.photo.save(
                temp_name,
                content=ContentFile(new_image_io.getvalue()),
                save=False
            )
        super(UserProfile, self).save(*args, **kwargs)

    class Meta:
        ordering = ['created_at']
