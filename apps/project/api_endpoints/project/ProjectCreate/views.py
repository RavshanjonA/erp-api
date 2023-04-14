from coreapi.auth import TokenAuthentication
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated

from .serializers import ProjectCreateSerializer
from apps.project.models import Project


class ProjectCreateView(CreateAPIView):
    permission_classes = [IsAuthenticated, ]
    authentication_classes = [TokenAuthentication, ]
    queryset = Project.objects.all()
    serializer_class = ProjectCreateSerializer


__all__ = ['ProjectCreateView']