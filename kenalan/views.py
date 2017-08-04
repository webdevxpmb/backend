from django.core.exceptions import PermissionDenied
from website.utils import StandardResultsSetPagination
from rest_framework.response import Response
from kenalan.models import (
    Token, Kenalan, KenalanStatus, DetailKenalan
)

from kenalan.serializers import( 
    TokenSerializer, KenalanSerializer,
    KenalanStatusSerializer, DetailKenalanSerializer,
    GetDetailKenalanSerializer, GetKenalanSerializer,
)

from rest_framework import generics, permissions
from account.permissions import(
    IsPmbAdmin,
    IsDetailKenalanOwner,
    IsKenalanOwner,
    is_maba,
    is_elemen,
    is_pmb_admin,
)


class TokenList(generics.ListAPIView):
    queryset = Token.objects.all()
    serializer_class = TokenSerializer
    permission_classes = (permissions.IsAdminUser,)


'''
Kenalan Views
'''


class KenalanList(generics.ListAPIView):
    serializer_class = KenalanSerializer
    permission_classes = (permissions.IsAuthenticated,)
    pagination_class = StandardResultsSetPagination
    filter_fields = ('user_elemen__profile__angkatan', )

    def get_queryset(self):
        if is_maba(self.request.user):
            queryset = Kenalan.objects.all().filter(user_maba=self.request.user)
        elif is_elemen(self.request.user):
            queryset = Kenalan.objects.all().filter(user_elemen=self.request.user)
        else:
            queryset = Kenalan.objects.all()

        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = GetKenalanSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = GetKenalanSerializer(queryset, many=True)
        return Response(serializer.data)


class KenalanDetail(generics.RetrieveUpdateAPIView):
    serializer_class = KenalanSerializer
    permission_classes = (IsKenalanOwner,)
    queryset = Kenalan.objects.all()

    def retrieve(self, request, *args, **kwargs):
        if is_pmb_admin(request.user):
            self.permission_classes = (IsPmbAdmin,)
        instance = self.get_object()
        serializer = GetKenalanSerializer(instance)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        if is_pmb_admin(request.user):
            self.permission_classes = (IsPmbAdmin,)
        if is_pmb_admin(request.user) or is_elemen(request.user):
            partial = kwargs.pop('partial', False)
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data, partial=partial)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)
            return Response(GetKenalanSerializer(instance).data)
        else:
            raise PermissionDenied


class KenalanStatusList(generics.ListCreateAPIView):
    queryset = KenalanStatus.objects.all()
    serializer_class = KenalanStatusSerializer
    permission_classes = (IsPmbAdmin,)


class KenalanStatusDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = KenalanStatus.objects.all()
    serializer_class = KenalanStatusSerializer
    permission_classes = (IsPmbAdmin,)


class DetailKenalanList(generics.ListAPIView):
    queryset = DetailKenalan.objects.all()
    serializer_class = DetailKenalanSerializer
    permission_classes = (permissions.IsAuthenticated,)
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        if is_maba(self.request.user):
            queryset = DetailKenalan.objects.all().filter(kenalan__user_maba=self.request.user)
        elif is_elemen(self.request.user):
            queryset = DetailKenalan.objects.all().filter(kenalan__user_elemen=self.request.user)
        else:
            queryset = DetailKenalan.objects.all()
        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = GetDetailKenalanSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = GetDetailKenalanSerializer(queryset, many=True)
        return Response(serializer.data)


class DetailKenalanDetail(generics.RetrieveUpdateAPIView):
    queryset = DetailKenalan.objects.all()
    serializer_class = DetailKenalanSerializer
    permission_classes = (IsDetailKenalanOwner,)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = GetDetailKenalanSerializer(instance)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        if is_pmb_admin(request.user) or is_maba(request.user):
            partial = kwargs.pop('partial', False)
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data, partial=partial)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)

            return Response(GetDetailKenalanSerializer(instance).data)
        else:
            raise PermissionDenied

