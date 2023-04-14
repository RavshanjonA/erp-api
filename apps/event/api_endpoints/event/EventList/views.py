from rest_framework.generics import ListAPIView

from apps.event.api_endpoints.event.EventList.serializers import EventListSerializer
from apps.event.models import Event


class EventListView(ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventListSerializer

__all__ = ['EventListView',]