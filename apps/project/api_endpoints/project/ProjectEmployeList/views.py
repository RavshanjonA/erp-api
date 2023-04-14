from django.views.generic import DetailView
from rest_framework.generics import RetrieveAPIView

from apps.project.api_endpoints.project.ProjectEmployeList.serializers import ProjectEmployeeSerializer
from apps.project.models import Project


class ProjectEmployesList(RetrieveAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectEmployeeSerializer
