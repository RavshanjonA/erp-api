from django.db.models import CharField, IntegerField, TimeField, FloatField, BooleanField
from rest_framework.fields import DecimalField

from apps.common.models import TimeStampedModel


class Employee(TimeStampedModel):
    first_name = CharField(max_length=28)
    last_name = CharField(max_length=28)
    age = IntegerField()
    salary = FloatField(default=0)
    start_work = TimeField()
    is_interner = BooleanField(default=False)

    class Meta:
        db_table = 'employee'
