from rest_framework.serializers import ModelSerializer

from apps.employee.models import Employee

class ShortEmployeeSerializer(ModelSerializer):
    model = Employee
    fields = ('id','first_name', 'last_name', 'age')


class ProjectEmployeeSerializer(ModelSerializer):
    def get_employess(self):
        return ShortEmployeeSerializer()
    class Meta:
        model = Employee
        fields = ('name','employess' )