from django.shortcuts import render
from rest_framework import generics

from dynamicqrcode.models import Dynamicqrcode
from .serializers import DynamicqrcodeSerializer
from rest_framework.pagination import LimitOffsetPagination

# Create your views here.


class DynamicqrcodeAPIView(generics.ListAPIView):
    queryset = Dynamicqrcode.objects.all()
    serializer_class = DynamicqrcodeSerializer
    paginator_class = LimitOffsetPagination