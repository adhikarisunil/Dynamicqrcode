from rest_framework import routers
from .viewsets import DynamicqrcodeModelViewSet

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'qrcode', DynamicqrcodeModelViewSet)