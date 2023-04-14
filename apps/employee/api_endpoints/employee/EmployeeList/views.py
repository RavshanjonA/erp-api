from rest_framework.generics import ListAPIView

from apps.employee.api_endpoints.employee.EmployeeList.serializers import EmployeeDetialSerializer
from apps.employee.models import Employee


class EmployeeListView(ListAPIView):
    serializer_class = EmployeeDetialSerializer
    queryset = Employee.objects.all()


__all__ = ['EmployeeListView', ]
