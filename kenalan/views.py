from django.core.exceptions import PermissionDenied
from rest_framework.response import Response
from kenalan.models import (
    Token, Kenalan, KenalanStatus, DetailKenalan
)

from kenalan.serializers import( 
    TokenSerializer, KenalanSerializer,
    KenalanStatusSerializer, DetailKenalanSerializer,
    GetDetailKenalanSerializer, GetKenalanSerializer,
    UserMabaSerializer, UserElemenSerializer,
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


# class TokenList(generics.ListAPIView):
#     queryset = Token.objects.all()
#     serializer_class = TokenSerializer
#     permission_classes = (permissions.IsAdminUser,)


'''
Kenalan Views
'''

DRAFT_STATUS = 'saved'
DRAFT_STATUS_ID = 4


class KenalanList(generics.ListCreateAPIView):
    serializer_class = KenalanSerializer
    permission_classes = (permissions.IsAuthenticated,)
    filter_fields = ('user_elemen__profile__angkatan', )

    def get_queryset(self):
        if is_maba(self.request.user):
            queryset = Kenalan.objects.all().filter(user_maba=self.request.user).order_by('-status', '-updated_at')
        elif is_elemen(self.request.user):
            queryset = Kenalan.objects.all().filter(user_elemen=self.request.user).exclude(status=DRAFT_STATUS_ID).order_by('-status', '-updated_at')
        else:
            queryset = Kenalan.objects.all()
        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
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
        if is_elemen(request.user):
            partial = kwargs.pop('partial', False)
            instance = self.get_object()
            if instance.status.status == 'pending':
                serializer = self.get_serializer(instance, data=request.data, partial=partial)
                serializer.is_valid(raise_exception=True)
                self.perform_update(serializer)
                return Response(GetKenalanSerializer(instance).data)
            else:
                raise PermissionDenied
        elif is_maba(request.user):
            partial = kwargs.pop('partial', False)
            instance = self.get_object()
            if instance.status.status == 'rejected' or instance.status.status == 'saved':
                data = request.data
                status = KenalanStatus.objects.get(id=data['status'])	
                if status.status != 'pending':	
                    raise PermissionDenied
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


class FriendList(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        if is_maba(self.request.user):
            queryset = Kenalan.objects.all().filter(user_maba=self.request.user)
        elif is_elemen(self.request.user):
            queryset = Kenalan.objects.all().filter(user_elemen=self.request.user)
        else:
            queryset = Kenalan.objects.all()

        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = GetKenalanSerializer(queryset, many=True)
        return Response(serializer.data)
