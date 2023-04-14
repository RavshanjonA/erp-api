from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import  RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

from .serializers import ProjectDetailSerializer
from apps.project.models import Project


class ProjectDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectDetailSerializer
    permission_classes = [IsAuthenticated, ]
    authentication_classes = [TokenAuthentication, ]


__all__ = ['ProjectDetailView',]