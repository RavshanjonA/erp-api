from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.permissions import  IsAuthenticatedOrReadOnly

from apps.event.api_endpoints.event.EventDetail.serializers import EventDetailSerializer
from apps.event.models import Event


class EventDetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly, ]
    authentication_classes = [TokenAuthentication, ]
    queryset = Event.objects.all()
    serializer_class = EventDetailSerializer

__all__ = ['EventDetailView']