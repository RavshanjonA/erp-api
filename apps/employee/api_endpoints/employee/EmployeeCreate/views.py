from rest_framework.generics import ListAPIView, CreateAPIView

from apps.employee.api_endpoints.employee.EmployeeCreate.serializers import EmployeeCreateSerializer
from apps.employee.models import Employee


class EmployeeCreateView(CreateAPIView):
    serializer_class = EmployeeCreateSerializer
    queryset = Employee.objects.all()



__all__ = [EmployeeCreateView, ]

