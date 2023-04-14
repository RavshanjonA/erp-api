from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated

from apps.event.api_endpoints.event.EventCreate.serializers import EventCreateSerializer
from apps.event.models import Event


class EventCreateView(CreateAPIView):
    serializer_class = EventCreateSerializer
    queryset = Event.objects.all()
    permission_classes = [IsAuthenticated, ]
    authentication_classes = [TokenAuthentication, ]


__all__ = ['EventCreateView' ]
