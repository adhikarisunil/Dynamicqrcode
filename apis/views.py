from django.shortcuts import render
from rest_framework import generics

from dynamicqrcode.models import Dynamicqrcode
from .serializers import DynamicqrcodeSerializer

# Create your views here.


class DynamicqrcodeAPIView(generics.ListAPIView):
    queryset = Dynamicqrcode.objects.all()
    serializer_class = DynamicqrcodeSerializer