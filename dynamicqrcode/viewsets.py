from rest_framework import viewsets
from .models import Dynamicqrcode
from .serializers import DynamicqrcodeSerializer
from rest_framework.permissions import IsAuthenticated
# from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import filters

# ViewSets define the view behavior.
class DynamicqrcodeModelViewSet(viewsets.ModelViewSet):
    queryset = Dynamicqrcode.objects.all()
    serializer_class = DynamicqrcodeSerializer
    permission_classes = [IsAuthenticated]
    # filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['name', 'qr_code_type']
    search_fields = ['name', 'qr_code_type']