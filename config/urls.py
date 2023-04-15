from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from config.schema import schema_url

urlpatterns = [
    path('attandance/', include('apps.attandance.urls')),
    path('employee/', include('apps.employee.urls')),
    path('event/', include('apps.event.urls')),
    path('internship/', include('apps.internship.urls')),
    path('inventory/', include('apps.inventory.urls')),
    path('project/', include('apps.project.urls')),
    path('admin/', admin.site.urls),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += schema_url