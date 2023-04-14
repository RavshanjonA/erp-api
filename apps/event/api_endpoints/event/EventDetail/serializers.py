from rest_framework.serializers import ModelSerializer

from apps.event.models import Event


class EventDetailSerializer(ModelSerializer):
    class Meta:
        model = Event
        fields = ('name', 'decription', 'date', 'created_at', 'updated_at')
