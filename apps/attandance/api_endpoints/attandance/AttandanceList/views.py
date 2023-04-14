from rest_framework.generics import ListAPIView

from .serializers import AttandanceListSerailizer
from apps.attandance.models import Attandance
from apps.employee.models import Employee


class AttandanceList(ListAPIView):
    queryset = Attandance.objects.all()
    serializer_class = AttandanceListSerailizer


__all__ = ['AttandanceList']
