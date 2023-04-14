from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated

from .serializers import InventoryCreateSerializer
from apps.inventory.models import Inventory


class InventoryCreateView(CreateAPIView):
    permission_classes = [IsAuthenticated, ]
    authentication_classes = [TokenAuthentication, ]
    queryset = Inventory.objects.all()
    serializer_class = InventoryCreateSerializer


__all__ = ['InventoryCreateView']
