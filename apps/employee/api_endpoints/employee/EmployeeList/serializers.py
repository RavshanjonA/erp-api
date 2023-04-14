from rest_framework.serializers import ModelSerializer

from apps.employee.models import Employee


class EmployeeDetialSerializer(ModelSerializer):
    class Meta:
        model = Employee
        fields = ('id','first_name', 'last_name', 'age', 'salary')
