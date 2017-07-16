from rest_framework import serializers
from django.contrib.auth.models import User
from account.models import (
    Role, Angkatan, UserProfile,
)

class RoleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Role
        fields = ('url', 'id', 'role_name')

class AngkatanSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Angkatan
        fields = ('url', 'id', 'year', 'name')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'password')

class UserProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('url', 'id', 'user', 'name', 'npm', 'email', 'role', 'angkatan', 'photo', 'about', 'linkedin', 'facebook', 'phone_number', 
                  'birth_place', 'birth_date', 'created_at', 'updated_at')

        extra_kwargs = {'role': {'read_only': True}, 'angkatan': {'read_only': True}, 
        				'npm': {'read_only': True}, 'user': {'read_only': True}}