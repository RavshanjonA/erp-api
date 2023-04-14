from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import  RetrieveUpdateDestroyAPIView
from rest_framework.permissions import  IsAuthenticatedOrReadOnly

from apps.employee.api_endpoints.employee.EmployeeDetail.serializers import EmployeeDetailSerializer
from apps.employee.models import Employee


class EmployeeDetialView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly, ]
    authentication_classes = [TokenAuthentication, ]
    serializer_class = EmployeeDetailSerializer
    queryset = Employee.objects.all()


__all__ = ['EmployeeDetialView', ]
