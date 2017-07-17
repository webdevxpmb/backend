from rest_framework import serializers
from django.contrib.auth.models import User
from account.models import (
    Role, Angkatan, UserProfile,
)

class RoleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Role
        fields = ('id', 'role_name')

class AngkatanSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Angkatan
        fields = ('id', 'year', 'name')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username',)

class UserProfileSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    role = serializers.PrimaryKeyRelatedField(read_only=True)
    angkatan = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = UserProfile
        fields = ('id', 'user', 'name', 'npm', 'email', 'role', 'angkatan', 'photo', 'about', 'linkedin', 'facebook', 'phone_number', 
                  'birth_place', 'birth_date', 'created_at', 'updated_at')

        extra_kwargs = {'role': {'read_only': True}, 'angkatan': {'read_only': True}, 
        				'npm': {'read_only': True}, 'user': {'read_only': True}}