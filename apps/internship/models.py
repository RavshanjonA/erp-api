from django.db.models import TextField, DateTimeField
from rest_framework.fields import CharField

from apps.common.models import TimeStampedModel


class Traniee(TimeStampedModel):
    first_name = CharField(max_length=128)
    last_name = CharField(max_length=128)

class Internship(TimeStampedModel):
    name = CharField(max_length=128)
    description = TextField()
    finished_at = DateTimeField()
