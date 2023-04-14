from django.urls import path

from apps.event.api_endpoints.event import EventCreateView, EventListView, EventDetailView

app_name = 'event'
urlpatterns = [
    path('', EventListView.as_view(), name='event-list'),
    path('create', EventCreateView.as_view(), name='event-crete'),
    path('<int:pk>/', EventDetailView.as_view(), name='event-detail')
]
