from rest_framework.serializers import ModelSerializer

from apps.attandance.models import Attandance


class AttandanceListSerailizer(ModelSerializer):
    class Meta:
        model = Attandance
        fields = ('employee', 'start_work')
