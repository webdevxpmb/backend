from kenalan.serializers import (
    KenalanSerializer
)

from kenalan.models import (
    Kenalan
)

from account.permissions import IsPmbAdmin
from rest_framework import generics
# Create your views here.

'''
Kenalan Views
'''


class KenalanList(generics.ListAPIView):
    serializer_class = KenalanSerializer
    permission_classes = (IsPmbAdmin,)
    queryset = Kenalan.objects.all()
    filter_fields = ('user_maba', 'user_elemen')


class KenalanDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = KenalanSerializer
    permission_classes = (IsPmbAdmin,)
    queryset = Kenalan.objects.all()

