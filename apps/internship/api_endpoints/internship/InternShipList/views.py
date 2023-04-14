from rest_framework.generics import ListAPIView

from apps.internship.api_endpoints.internship.InternShipList.serializers import InternshipListSerializer
from apps.internship.models import Internship


class InternshipListView(ListAPIView):
    queryset = Internship.objects.all()
    serializer_class = InternshipListSerializer