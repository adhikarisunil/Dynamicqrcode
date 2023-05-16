from django.urls import path
from .views import DynamicqrcodeListView
from .views import DynamicqrcodeAPIView

urlpatterns = [
    path("", DynamicqrcodeListView.as_view(), name="home"),
    path("", DynamicqrcodeAPIView.as_view(), name="dynamicqrcode_list"),
]