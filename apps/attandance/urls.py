from django.urls import path
from .api_endpoints import attandance

app_name = 'attandance'
urlpatterns = [
    path('', attandance.AttandanceList.as_view(), name='attandances'),
    path('<int:pk>', attandance.AttandanceDetailView.as_view(), name='attandance-detail')
]
