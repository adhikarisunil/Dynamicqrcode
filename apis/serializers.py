# apis/serializers.py
from rest_framework import serializers
from dynamicqrcode.models import Dynamicqrcode


class DynamicqrcodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dynamicqrcode
        fields = ("name", "type", "content", "start_date", "end_date","is_active")