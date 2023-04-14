from rest_framework.generics import CreateAPIView

from apps.inventory.api_endpoints.inventory.InventoryCreate.serializers import InventoryCreateSerializer
from apps.inventory.models import Inventory


class InventoryCreateView(CreateAPIView):
    queryset = Inventory.objects.all()
    serializer_class = InventoryCreateSerializer
