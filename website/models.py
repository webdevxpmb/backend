from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class PostType(models.Model):
    post_type = models.CharField(max_length=50)

    def __str__(self):
        return self.post_type

    class Meta:
        pass


class Post(models.Model):
    """
    Description: Model Description
    """
    title = models.CharField(max_length=50, null=True)
    author = models.ForeignKey(User, related_name="post")
    summary = models.CharField(max_length=255, blank=True, null=True)
    content = models.TextField()
    attachment_link = models.CharField(max_length=255, blank=True, null=True)
    post_type = models.ForeignKey(PostType, related_name='post')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        pass


class Comment(models.Model):
    """
    Description: Model Description
    """
    post = models.ForeignKey(Post, related_name="comments")
    author = models.ForeignKey(User, related_name="comments")
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        pass


class ElementWord(models.Model):
    """
    Description: Model Description
    """
    author = models.ForeignKey(User, related_name="element_words")
    testimony = models.TextField()
    approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        pass


class Task(models.Model):

    def __str__(self):
        return self.name
    """
    Description: Model Description
    """
    name = models.CharField(max_length=255, null=True)
    description = models.TextField(blank=True, null=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    attachment_link = models.CharField(max_length=255, blank=True, null=True)
    is_kenalan = models.BooleanField(default=False)
    expected_amount_omega = models.SmallIntegerField(blank=True, null=True)
    expected_amount_capung = models.SmallIntegerField(blank=True, null=True)
    expected_amount_orion = models.SmallIntegerField(blank=True, null=True)
    expected_amount_alumni = models.SmallIntegerField(blank=True, null=True)
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
    file_link = models.CharField(max_length=255, null=True)
    is_checked = models.BooleanField(default=False)
    is_approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        pass


class Event(models.Model):

    def __str__(self):
        return self.name

    """
    Description: Model Description
    """
    name = models.CharField(max_length=255, null=True)
    description = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=255)
    start_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)
    attachment_link = models.CharField(max_length=255, blank=True, null=True)
    expected_attendee = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        pass


class Album(models.Model):
    name = models.CharField(max_length=255)
    album_link = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        pass


class TaskStatistic(models.Model):
    task = models.ForeignKey(Task, related_name='statistics')
    amount = models.SmallIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        pass


class EventStatistic(models.Model):
    event = models.ForeignKey(Event)
    attendee = models.SmallIntegerField(default=0)
    on_time = models.SmallIntegerField(default=0)
    late = models.SmallIntegerField(default=0)
    permission = models.SmallIntegerField(default=0)
    absent = models.SmallIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        pass


class UserStatistic(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(User)
    task = models.ForeignKey(Task)
    amount_omega = models.SmallIntegerField(default=0)
    amount_capung = models.SmallIntegerField(default=0)
    amount_orion = models.SmallIntegerField(default=0)
    amount_alumni = models.SmallIntegerField(default=0)
    amount_total = models.SmallIntegerField(default=0)
    amount_approved_omega = models.SmallIntegerField(default=0)
    amount_approved_capung = models.SmallIntegerField(default=0)
    amount_approved_orion = models.SmallIntegerField(default=0)
    amount_approved_alumni = models.SmallIntegerField(default=0)
    amount_approved_total = models.SmallIntegerField(default=0)

    class Meta:
        pass


class Vote(models.Model):
    def __str__(self):
        return self.title


    title = models.CharField(max_length=500)
    description = models.CharField(max_length=500, null=True, blank=True)
    start_time = models.DateTimeField(null=True, blank=True)
    end_time = models.DateTimeField(null=True, blank=True)
    total_voters = models.SmallIntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class meta:
        pass


class VoteOption(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=500)
    description = models.CharField(max_length=500, null=True, blank=True)
    vote = models.ForeignKey(Vote, on_delete=models.CASCADE, related_name='options')
    total_voters = models.SmallIntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        pass
    

class Voting(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='votings')
    vote_option = models.ForeignKey(VoteOption, on_delete=models.CASCADE, related_name='votings')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        unique_together = ("user", "vote_option",)