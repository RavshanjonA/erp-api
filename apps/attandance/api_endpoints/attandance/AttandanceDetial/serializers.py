from rest_framework.serializers import ModelSerializer

from apps.attandance.models import Attandance
from apps.employee.models import Employee


class CustomEmployeeSerializer(ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id', 'first_name', 'last_name', 'is_interner']


class AttandanceDetailSerailizer(ModelSerializer):
    employee = CustomEmployeeSerializer()

    class Meta:
        model = Attandance
        fields = ('employee', 'start_work')
