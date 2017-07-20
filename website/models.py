from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Post(models.Model):
    """
    Description: Model Description
    """
    title = models.CharField(max_length=50, null=True)
    author = models.ForeignKey(User, related_name="post")
    summary =  models.CharField(max_length=255, null=True)
    content = models.TextField(null=True)
    post_type = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        pass


class Comments(models.Model):
    """
    Description: Model Description
    """
    post = models.ForeignKey(Post, related_name="comments")
    author = models.ForeignKey(User, related_name="comments")
    comment = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        pass


class ElementWord(models.Model):
    """
    Description: Model Description
    """
    author = models.ForeignKey(User, related_name="elementwords")
    testimony = models.TextField(null=True)
    approved = models.BooleanField( default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        pass


class Task(models.Model):
    """
    Description: Model Description
    """
    name = models.CharField(max_length=50,null=True)
    description = models.TextField(null=True)
    author = models.ForeignKey(User, related_name="task")
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    type = models.CharField(max_length=50,null=True)
    amount = models.IntegerField(null=True)
    expected_amount = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        pass


class Submission(models.Model):
    """
    Description: Model Description
    """
    user = models.ForeignKey(User, related_name="submissions")
    task = models.ForeignKey(Task, related_name="submissions")
    file = models.FileField(upload_to="uploads/", null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Events(models.Model):
    """
    Description: Model Description
    """
    name = models.CharField(max_length=50, null=True)
    description = models.TextField(null=True)
    author = models.ForeignKey(User, related_name="event")
    location = models.CharField(max_length=50)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    type = models.CharField(max_length=50, null=True)
    attendee = models.IntegerField(null=True)
    expected_attendee = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        pass


class Attachment(models.Model):
    """
    Description: Model Description
    """
    filename = models.CharField(max_length=50, null=True)
    url = models.FileField(upload_to="uploads/", null=True)
    events = models.ForeignKey(Events, related_name="attachments", null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        pass