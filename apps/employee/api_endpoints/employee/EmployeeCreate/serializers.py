from rest_framework.serializers import ModelSerializer

from apps.employee.models import Employee


class EmployeeCreateSerializer(ModelSerializer):
    class Meta:
        model = Employee
        fields = ('first_name', 'last_name', 'age', 'salary', 'start_work')
