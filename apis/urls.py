from django.urls import path
from .views import DynamicqrcodeAPIView

urlpatterns = [
path("", DynamicqrcodeAPIView.as_view(), name="dynamicqrcode_list"),
]