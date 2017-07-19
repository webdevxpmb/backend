from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Attachment(models.Model):
    """
    Description: Model Description
    """
    filename = models.CharField(max_length=50, null=True)
    url = models.FileField(upload_to="uploads/", null=True)

    class Meta:
        pass

class PostType(models.Model):
    """
    Description: Model Description
    """
    post_type = models.CharField(max_length=50,null=True)

    class Meta:
        pass

class Post(models.Model):
    """
    Description: Model Description
    """
    title = models.CharField(max_length=50, null=True)
    author = models.ForeignKey(User, related_name="post")
    summary =  models.CharField(max_length=255, null=True)
    content = models.TextField(null=True)
    post_type = models.ForeignKey(PostType, related_name="post_type")
    attachment = models.ForeignKey(Attachment, related_name="post_attachment")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        pass


class Comments(models.Model):
    """
    Description: Model Description
    """
    post = models.ForeignKey(Post, related_name="comments")
    author = models.ForeignKey(User, related_name="author")
    comment = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        pass


class ElementWord(models.Model):
    """
    Description: Model Description
    """
    author = models.ForeignKey(User, related_name="element_author")
    testimony = models.TextField(null=True)
    approved = models.BooleanField( default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        pass


class Submission(models.Model):
    """
    Description: Model Description
    """
    user = models.ForeignKey(User, related_name="submission")
    attachment = models.ForeignKey(Attachment,related_name="submission")
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
    submission = models.ForeignKey(Submission, related_name="task")
    amount = models.IntegerField(null=True)
    expected_amount = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        pass


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
    submission = models.ForeignKey(Submission, related_name="event")
    attendee = models.IntegerField(null=True)
    expected_attendee = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        pass