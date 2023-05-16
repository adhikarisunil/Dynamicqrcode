from rest_framework import viewsets
from .models import Dynamicqrcode
from .serializers import DynamicqrcodeSerializer

# ViewSets define the view behavior.
class DynamicqrcodeModelViewSet(viewsets.ModelViewSet):
    queryset = Dynamicqrcode.objects.all()
    serializer_class = DynamicqrcodeSerializer