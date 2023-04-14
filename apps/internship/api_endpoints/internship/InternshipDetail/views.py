from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import  RetrieveUpdateDestroyAPIView
from rest_framework.permissions import  IsAuthenticatedOrReadOnly

from .serializers import InternshipDetailSerializer
from apps.internship.models import Internship


class InternshipDetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly, ]
    authentication_classes = [TokenAuthentication, ]
    queryset = Internship.objects.all()
    serializer_class = InternshipDetailSerializer

__all__ = ['InternshipDetailView']