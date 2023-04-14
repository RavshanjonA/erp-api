from coreapi.auth import TokenAuthentication
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.permissions import  IsAuthenticatedOrReadOnly

from apps.inventory.api_endpoints.inventory.InventoryDetail.serializers import InventoryDetailSerializer
from apps.inventory.models import Inventory



class InvertoryDetiaView(RetrieveUpdateDestroyAPIView):
    queryset = Inventory.objects.all()
    serializer_class = InventoryDetailSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, ]
    authentication_classes = [TokenAuthentication, ]


__all__ = ['InvertoryDetiaView',]