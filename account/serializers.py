from rest_framework import serializers
from django.contrib.auth.models import User
from account.models import (
    Role, Angkatan, UserProfile,
)

from backend.settings import HOST_URL


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
                  'photo', 'about', 'asal_sekolah', 'link_gdrive', 'line_id', 'phone_number',
                  'birth_place', 'birth_date', 'score', 'created_at', 'updated_at')
        read_only_fields = ('role', 'npm', 'angkatan', 'user', 'name', )


class GetUserProfileSerializer(serializers.ModelSerializer):
    role = RoleSerializer()
    angkatan = AngkatanSerializer()
    photo_url = serializers.SerializerMethodField()
    class Meta:
        model = UserProfile
        fields = ('id', 'user', 'name', 'role', 'npm', 'angkatan', 'email',
                  'photo', 'about', 'asal_sekolah', 'link_gdrive', 'line_id', 'phone_number',
                  'birth_place', 'birth_date', 'score', 'created_at', 'updated_at', 'photo_url')
        read_only_fields = ('role', 'npm', 'angkatan', 'user')

    def get_photo_url(self, user_profile):
        if user_profile.photo:
            photo_url = HOST_URL + user_profile.photo.url
            return photo_url
        else:
            return None


class ShrinkedUserProfileSerializer(serializers.ModelSerializer):
    angkatan = AngkatanSerializer()
    photo_url = serializers.SerializerMethodField()

    class Meta:
        model = UserProfile
        fields = ('id', 'name', 'npm', 'angkatan', 'email', 'photo', 'photo_url')

    def get_photo_url(self, user_profile):
        if user_profile.photo:
            photo_url = HOST_URL + user_profile.photo.url
            return photo_url
        else:
            return None


class UserSerializer(serializers.ModelSerializer):
    profile = ShrinkedUserProfileSerializer()

    class Meta:
        model = User
        fields = ('id', 'username', 'profile')


class DetailUserSerializer(serializers.ModelSerializer):
    profile = GetUserProfileSerializer()

    class Meta:
        model = User
        fields = ('id', 'username', 'profile')
