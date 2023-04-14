from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated

from apps.employee.api_endpoints.employee.EmployeeCreate.serializers import EmployeeCreateSerializer
from apps.employee.models import Employee


class EmployeeCreateView(CreateAPIView):
    permission_classes = [IsAuthenticated, ]
    authentication_classes = [TokenAuthentication, ]
    serializer_class = EmployeeCreateSerializer
    queryset = Employee.objects.all()


__all__ = ['EmployeeCreateView', ]
