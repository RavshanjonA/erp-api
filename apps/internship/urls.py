from django.urls import path
from .api_endpoints import internship


app_name = 'internship'
urlpatterns = [
    path('', internship.InternshipListView.as_view(), name='internship-list'),
    path('<int:pk>', internship.InternshipDetailView.as_view(), name='internship-detail'),
    path('create/', internship.InternShipCreateView.as_view(), name='internship-create'),

]
