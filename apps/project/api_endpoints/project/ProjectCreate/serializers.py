from rest_framework.serializers import ModelSerializer

from apps.project.models import Project


class ProjectCreateSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = ('name', 'decription', 'employess', 'deadline')