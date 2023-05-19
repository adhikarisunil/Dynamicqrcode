from django.urls import path
from .views import DynamicqrcodeListView
from .views import DynamicqrcodeAPIView

urlpatterns = [
    path("api/", DynamicqrcodeListView.as_view(), name="home"),
    path("api/", DynamicqrcodeAPIView.as_view(), name="dynamicqrcode_list"),
]