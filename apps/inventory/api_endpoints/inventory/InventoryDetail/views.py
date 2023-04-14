from rest_framework.generics import RetrieveAPIView

from apps.inventory.api_endpoints.inventory.InventoryDetail.serializers import InventoryDetailSerializer
from apps.inventory.models import Inventory


class InvertoryDetiaView(RetrieveAPIView):
    queryset = Inventory.objects.all()
    serializer_class = InventoryDetailSerializer


__all__ = [InvertoryDetiaView,]