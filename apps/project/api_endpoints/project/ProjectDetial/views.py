from rest_framework.generics import RetrieveAPIView

from apps.project.api_endpoints.project.ProjectDetial.serializers import ProjectDetailSerializer
from apps.project.models import Project


class ProjectDetailView(RetrieveAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectDetailSerializer