from django.urls import path

from apps.employee.api_endpoints import employee

app_name = 'employee'

urlpatterns = [
    path('', employee.EmployeeListView.as_view(), name='employee-list'),
    path('create', employee.EmployeeCreateView.as_view(), name='employee-create'),
    path('<int:pk>', employee.EmployeeDetialView.as_view(), name='employee-detail')

]
