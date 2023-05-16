from rest_framework import generics

from .serializers import DynamicqrcodeSerializer 
from django.views.generic import ListView
from .models import Dynamicqrcode

class DynamicqrcodeListView(ListView):
    model = Dynamicqrcode
    template_name = "dynamicqrcode_list.html"


class DynamicqrcodeAPIView(generics.ListAPIView):
    queryset = Dynamicqrcode.objects.all()
    serializer_class = DynamicqrcodeSerializer




