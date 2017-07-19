from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from website.serializers import (
    AttachmentSerializer
)
from website.models import (
    Attachment
)

# Create your views here.
class AttachmentList(generics.ListAPIView):
    queryset = Attachment.objects.all()
    serializer_class = AttachmentSerializer

