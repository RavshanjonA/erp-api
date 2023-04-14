from rest_framework.generics import RetrieveAPIView

from apps.employee.api_endpoints.employee.EmployeeDetail.serializers import EmployeeDetailSerializer
from apps.employee.models import Employee


class EmployeeDetialView(RetrieveAPIView):
    serializer_class = EmployeeDetailSerializer
    queryset = Employee.objects.all()


__all__ = [EmployeeDetialView, ]
