from rest_framework import serializers
from django.contrib.auth.models import User
from kenalan.models import (
    Token, Kenalan, KenalanStatus, KenalanDetail
)



class TokenSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Token
        fields = ('token', 'user', 'start_time', 'end_time','created_at', 'updated_at')

class KenalanSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Kenalan
        fields = ('url', 'id', 'user1', 'user2','created_at', 'updated_at')

class KenalanStatusSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = KenalanStatus
        fields = ('url', 'id', 'status','created_at', 'updated_at')

class KenalanDetailSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = KenalanDetail
        fields = ('url', 'id', 'kenalan', 'status', 'name', 'phone_number', 'birth_place', 
                  'birth_date', 'asal_sma', 'story', 'created_at', 'updated_at')