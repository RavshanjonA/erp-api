from rest_framework.generics import RetrieveAPIView

from apps.internship.api_endpoints.internship.InternshipDetail.serializers import InternshipDetailSerializer
from apps.internship.models import Internship


class InternshipDetailView(RetrieveAPIView):
    queryset = Internship.objects.all()
    serializer_class = InternshipDetailSerializer