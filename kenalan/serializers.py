from rest_framework import serializers
from kenalan.models import (
    Token, Kenalan, KenalanStatus, DetailKenalan
)

from account.serializers import DetailUserSerializer, UserSerializer


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
    user_elemen = DetailUserSerializer()
    user_maba = DetailUserSerializer()
    detail_kenalan = ShrinkedDetailKenalanSerializer()

    class Meta:
        model = Kenalan
        fields = ('detail_kenalan', 'id', 'user_elemen', 'user_maba', 'status', 'created_at', 'updated_at')
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
    user_elemen = DetailUserSerializer()

    class Meta:
        model = Kenalan
        read_only_fields = fields = ('user_elemen', )


class UserMabaSerializer(serializers.ModelSerializer):
    user_maba = DetailUserSerializer()

    class Meta:
        model = Kenalan
        read_only_fields = fields = ('user_maba', )



