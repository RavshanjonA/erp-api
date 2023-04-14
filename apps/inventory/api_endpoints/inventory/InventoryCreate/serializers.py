from rest_framework.serializers import ModelSerializer

from apps.inventory.models import Inventory


class InventoryCreateSerializer(ModelSerializer):
    class Meta:
        model = Inventory
        fields = ('name', 'description')
