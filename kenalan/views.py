from django.contrib.auth.models import User
from django.utils import timezone

from kenalan.models import (
    Token, Kenalan, KenalanStatus, DetailKenalan
)

from kenalan.serializers import( 
    TokenSerializer, KenalanSerializer,
    KenalanStatusSerializer, DetailKenalanSerializer,
)

from rest_framework import generics, permissions

from kenalan.utils import(
    is_maba,
    is_elemen,
    is_akademis,
)

from account.permissions import(
    IsOwner,
    IsAkademis,
    IsElemen,
    IsMaba,
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

    def get_queryset(self):
        if is_maba(self.request):
            queryset = Kenalan.objects.all().filter(user_maba=self.request.user)
        elif is_elemen(self.request):
            queryset = Kenalan.objects.all().filter(user_elemen=self.request.user)
        else:
            queryset = Kenalan.objects.all()

        return queryset

class KenalanDetail(generics.RetrieveUpdateAPIView):
    serializer_class = KenalanSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        if is_maba(self.request):
            queryset = Kenalan.objects.all().filter(user_maba=self.request.user)
        elif is_elemen(self.request):
            queryset = Kenalan.objects.all().filter(user_elemen=self.request.user)
        else:
            queryset = Kenalan.objects.all()
            
        return queryset

    def put(self, request, pk, format=None):
        kenalan = self.get_object(pk)
        if is_elemen(request) or is_akademis(request):
            serializer = KenalanSerializer(kenalan, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=400)
        else:
            raise PermissionDenied({"message":"You don't have permission to access"})


class KenalanStatusList(generics.ListAPIView):
    queryset = KenalanStatus.objects.all()
    serializer_class = KenalanStatusSerializer
    # permission_classes = (permissions.IsAuthenticated,)

class KenalanStatusDetail(generics.RetrieveAPIView):
    queryset = KenalanStatus.objects.all()
    serializer_class = KenalanStatusSerializer
    # permission_classes = (permissions.IsAuthenticated,)

class DetailKenalanList(generics.ListAPIView):
    queryset = DetailKenalan.objects.all()
    serializer_class = DetailKenalanSerializer
    # permission_classes = (permissions.IsAuthenticated,)

class DetailKenalanDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = DetailKenalan.objects.all()
    serializer_class = DetailKenalanSerializer
    # permission_classes = (permissions.IsAuthenticated,)
    
