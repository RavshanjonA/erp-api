from rest_framework.serializers import ModelSerializer

from apps.inventory.models import Inventory


class InventoryDetailSerializer(ModelSerializer):
    class Meta:
        model = Inventory
        fields = ('name','description', 'created_at', 'updated_at')
