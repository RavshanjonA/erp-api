from rest_framework.serializers import ModelSerializer

from apps.internship.models import Internship


class InternshipListSerializer(ModelSerializer):
    class Meta:
        model = Internship
        fields = ('name', 'description', 'finished')

