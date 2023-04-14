from rest_framework.serializers import ModelSerializer

from apps.internship.models import Internship


class InternshipDetailSerializer(ModelSerializer):
    class Meta:
        model = Internship
        fields = ('name', 'description', 'finished_at', 'created_at', 'updated_at')
