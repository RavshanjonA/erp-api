from django.urls import path
from .api_endpoints import inventory

urlpatterns = [
    path('', inventory.InvertoryListView.as_view(), name='ineventory-list'),
    path('<int:pk>', inventory.InvertoryDetiaView.as_view(), name='ineventory-list'),
    path('create/', inventory.InventoryCreateView.as_view(), name='ineventory-create'),
]
