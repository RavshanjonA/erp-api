from django.urls import path
from .api_endpoints import project

app_name = 'project'
urlpatterns = [
    path('', project.ProjectListView.as_view(), name='project-list'),
    path('create', project.ProjectCreateView.as_view(), name='project-create'),
    path('<int:pk>', project.ProjectDetailView.as_view(), name='project-detail'),
]
