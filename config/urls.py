from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework.permissions import AllowAny

scheme_view = get_schema_view(
    openapi.Info(
        title="ERP App REST API",
        default_version="v1",
        description="Swagger docs for REST API",
        contact=openapi.Contact('Ravshanjon Ahmadjonov akhamdjonovr.98@gmail.com')
    ),
    public=True,
    permission_classes=(AllowAny,)
)

urlpatterns = [
    # doc
    path('', scheme_view.with_ui('swagger', cache_timeout=0), name="swagger-docs"),
    path('redocs/', scheme_view.with_ui('redoc', cache_timeout=0), name="redoc-docs"),
    # local apps
    path('attandance/', include('apps.attandance.urls')),
    path('employee/', include('apps.employee.urls')),
    path('event/', include('apps.event.urls')),
    path('internship/', include('apps.internship.urls')),
    path('inventory/', include('apps.inventory.urls')),
    path('project/', include('apps.project.urls')),

    # admin
    path('admin/', admin.site.urls),
]
