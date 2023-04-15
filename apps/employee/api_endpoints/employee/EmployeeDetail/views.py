from datetime import timedelta

from django.db.models import Sum, Func, F, Value, IntegerField
from django.db.models.functions import Least, TruncTime
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
    def get_queryset(self):
        queryset =  super().get_queryset()
        qs = queryset.annotate(
            delay_time=Sum(Least(
                Func(
                    F('attandanes__start_work') - Value(timedelta(hours=9)),
                    function=TruncTime
                ),
                Value(0)
            )) / 60,
            output_field=IntegerField()
        ).values()

        return qs
__all__ = ['EmployeeDetialView', ]
