from rest_framework.generics import ListAPIView

from .serializers import ProjectListSerializer
from apps.project.models import Project


class ProjectListView(ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectListSerializer


__all__ = ['ProjectListView', ]
