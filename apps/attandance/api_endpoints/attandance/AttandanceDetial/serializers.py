from rest_framework.serializers import ModelSerializer

from apps.attandance.models import Attandance


class AttandanceDetailSerailizer(ModelSerializer):
    class Meta:
        model = Attandance
        fields = ('user','start_work')
