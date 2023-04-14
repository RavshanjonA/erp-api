from rest_framework.generics import CreateAPIView

from apps.project.api_endpoints.project.ProjectCreate.serializers import ProjectCreateSerializer
from apps.project.models import Project


class ProjectCreateView(CreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectCreateSerializer
