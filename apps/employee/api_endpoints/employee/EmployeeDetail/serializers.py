from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer, IntegerField

from apps.employee.models import Employee


class EmployeeDetailSerializer(ModelSerializer):
    delay_time = SerializerMethodField()
    class Meta:
        model = Employee
        fields = ('first_name', 'last_name', 'age', 'salary', 'start_work', 'created_at', 'delay_time')
    def get_delay_time(self, obj):
        return obj.delay_time