from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('attandance/', include('apps.attandance.urls')),
    path('employee/', include('apps.employee.urls')),
    path('event/', include('apps.event.urls')),
    path('internship/', include('apps.internship.urls')),
    path('inventory/', include('apps.inventory.urls')),
    path('project/', include('apps.project.urls')),
    path('admin/', admin.site.urls),
]

