from rest_framework import serializers
from django.contrib.auth.models import User
from account.models import (
    Role, Angkatan, UserProfile,
)


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ('id', 'role_name')


class AngkatanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Angkatan
        fields = ('id', 'year', 'name')


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('id', 'user', 'name', 'role', 'npm', 'angkatan', 'email',
                  'photo', 'about', 'linkedin', 'facebook', 'phone_number',
                  'birth_place', 'birth_date', 'created_at', 'updated_at')
        read_only_fields = ('role', 'npm', 'angkatan', 'user')


class UserSerializer(serializers.ModelSerializer):
    profile = UserProfileSerializer()
    class Meta:
        model = User
        fields = ('id', 'username', 'profile')
