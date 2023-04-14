from rest_framework.serializers import ModelSerializer

from apps.internship.models import Internship


class InternshipCreateSerializer(ModelSerializer):
    class Meta:
        model = Internship
        fields = ('name', 'description', 'finished_at')
