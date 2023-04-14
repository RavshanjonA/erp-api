from rest_framework.serializers import ModelSerializer

from apps.event.models import Event


class EventCreateSerializer(ModelSerializer):
    class Meta:
        model = Event
        fields = ('name', 'decription', 'date')
