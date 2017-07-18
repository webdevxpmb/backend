from rest_framework import serializers
from django.contrib.auth.models import User
from kenalan.models import (
    Token, Kenalan, KenalanStatus, DetailKenalan
)

from account.serializers import( 
    UserSerializer, RoleSerializer,
    AngkatanSerializer, UserProfileSerializer,
)



class TokenSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Token
        fields = ('token', 'user', 'start_time', 'end_time','created_at', 'updated_at')

class KenalanSerializer(serializers.HyperlinkedModelSerializer):
    detail = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    user_elemen = serializers.PrimaryKeyRelatedField(read_only=True)
    user_maba =  serializers.PrimaryKeyRelatedField(read_only=True)
    status =  serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Kenalan
        fields = ('detail', 'id', 'user_elemen', 'user_maba', 'status')
        extra_kwargs = {'user_elemen': {'read_only': True},
                        'user_maba': {'read_only': True}}

class KenalanStatusSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = KenalanStatus
        fields = ('id', 'status')

class DetailKenalanSerializer(serializers.HyperlinkedModelSerializer):
    kenalan =  serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = DetailKenalan
        fields = ('id', 'kenalan', 'name', 'phone_number', 'birth_place', 
                  'birth_date', 'asal_sma', 'story', 'created_at', 'updated_at')
        extra_kwargs = {'kenalan': {'read_only': True}}