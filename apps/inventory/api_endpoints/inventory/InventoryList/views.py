from rest_framework.generics import ListAPIView

from apps.inventory.api_endpoints.inventory.InventoryList.serializers import InventoryListSerializer
from apps.inventory.models import Inventory


class InvertoryListView(ListAPIView):
    queryset = Inventory.objects.all()
    serializer_class = InventoryListSerializer


__all__ = [InvertoryListView,]