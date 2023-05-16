from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Dynamicqrcode


class DynamicqrcodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dynamicqrcode
        fields =("url", "id", "name", "type", "content", "start_date", "end_date", "is_active")