from rest_framework.serializers import ModelSerializer

from apps.employee.api_endpoints.employee.EmployeeDetail.serializers import EmployeeDetailSerializer
from apps.project.models import Project


class ProjectDetailSerializer(ModelSerializer):
    class Meta:
        model= Project
        fields = ('name', 'decription', 'employess', 'status', 'deadline')