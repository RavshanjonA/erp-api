from django.db.models import CharField, IntegerField, TimeField
from rest_framework.fields import  DecimalField

from apps.common.models import TimeStampedModel


class Employee(TimeStampedModel):
    first_name = CharField(max_length=28)
    last_name = CharField(max_length=28)
    age = IntegerField()
    salary = DecimalField(decimal_places=2, max_digits=15, default=0)
    start_work = TimeField()
    end_work = TimeField()

