from rest_framework import serializers
from django.contrib.auth.models import User
from website.models import (
    Attachment, PostType, Post, Comments,
    ElementWord, Submission, Task,
)