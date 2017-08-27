from rest_framework import serializers
from kenalan.models import (
    Token, Kenalan, KenalanStatus, DetailKenalan
)

from account.serializers import UserSerializer


class TokenSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Token
        fields = read_only_fields = ('token', 'user', 'start_time', 'end_time', 'created_at', 'updated_at')


class KenalanStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = KenalanStatus
        fields = ('id', 'status')


class KenalanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kenalan
        fields = ('id', 'user_elemen', 'user_maba', 'status')
        read_only_fields = ('user_elemen', 'user_maba')


class ShrinkedDetailKenalanSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetailKenalan
        fields = ('id', 'name', 'phone_number', 'birth_place',
                  'birth_date', 'asal_sma', 'story', 'created_at', 'updated_at')
        read_only_fields = ('kenalan',)


class GetKenalanSerializer(serializers.ModelSerializer):
    status = KenalanStatusSerializer()
    user_elemen = UserSerializer()
    user_maba = UserSerializer()
    detail_kenalan = ShrinkedDetailKenalanSerializer()

    class Meta:
        model = Kenalan
        fields = ('detail_kenalan', 'id', 'user_elemen', 'user_maba', 'status')
        read_only_fields = ('detail_kenalan', 'user_elemen', 'user_maba')


class DetailKenalanSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetailKenalan
        fields = ('id', 'kenalan', 'name', 'phone_number', 'birth_place', 
                  'birth_date', 'asal_sma', 'story', 'created_at', 'updated_at')
        read_only_fields = ('kenalan',)


class GetDetailKenalanSerializer(serializers.ModelSerializer):
    kenalan = KenalanSerializer()

    class Meta:
        model = DetailKenalan
        fields = ('id', 'kenalan', 'name', 'phone_number', 'birth_place',
                  'birth_date', 'asal_sma', 'story', 'created_at', 'updated_at')
        read_only_fields = ('kenalan',)



class UserElemenSerializer(serializers.ModelSerializer):
    user_elemen = UserSerializer()

    class Meta:
        model = Kenalan
        read_only_fields = fields = ('user_elemen', )


class UserMabaSerializer(serializers.ModelSerializer):
    user_maba = UserSerializer()

    class Meta:
        model = Kenalan
        read_only_fields = fields = ('user_maba', )



