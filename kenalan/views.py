from django.contrib.auth.models import User
from django.utils import timezone

from kenalan.models import (
    Token, Kenalan, KenalanStatus, KenalanDetail as KD
)

from kenalan.serializers import( 
    TokenSerializer, KenalanSerializer,
    KenalanStatusSerializer, KenalanDetailSerializer,
)

from rest_framework import generics, permissions


class TokenList(generics.ListAPIView):
    queryset = Token.objects.all()
    serializer_class = TokenSerializer
    filter_fields = ['user']
    permission_classes = (permissions.IsAuthenticated,)

class TokenDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Token.objects.all()
    serializer_class = TokenSerializer
    permission_classes = (permissions.IsAuthenticated,)

class TokenCreate(generics.CreateAPIView):
    queryset = Token.objects.all()
    serializer_class = TokenSerializer
    permission_classes = (permissions.IsAuthenticated,)

class KenalanList(generics.ListCreateAPIView):
    queryset = Kenalan.objects.all()
    serializer_class = KenalanSerializer
    filter_fields = ['token', 'user1', 'user2']
    permission_classes = (permissions.IsAuthenticated,)

class KenalanDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Kenalan.objects.all()
    serializer_class = KenalanSerializer
    permission_classes = (permissions.IsAuthenticated,)

class KenalanStatusList(generics.ListCreateAPIView):
    queryset = KenalanStatus.objects.all()
    serializer_class = KenalanStatusSerializer
    permission_classes = (permissions.IsAuthenticated,)

class KenalanStatusDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = KenalanStatus.objects.all()
    serializer_class = KenalanStatusSerializer
    permission_classes = (permissions.IsAuthenticated,)

class KenalanDetailList(generics.ListCreateAPIView):
    queryset = KD.objects.all()
    serializer_class = KenalanDetailSerializer
    filter_fields = ['status', 'kenalan']
    permission_classes = (permissions.IsAuthenticated,)

class KenalanDetailDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = KD.objects.all()
    serializer_class = KenalanDetailSerializer
    permission_classes = (permissions.IsAuthenticated,)
    