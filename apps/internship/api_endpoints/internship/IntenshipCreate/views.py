from coreapi.auth import TokenAuthentication
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated

from .serializers import InternshipCreateSerializer
from apps.internship.models import Internship


class InternShipCreateView(CreateAPIView):
    permission_classes = [IsAuthenticated, ]
    authentication_classes = [TokenAuthentication, ]
    queryset = Internship.objects.all()
    serializer_class = InternshipCreateSerializer


__all__ = ['InternShipCreateView']