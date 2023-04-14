from django.db import models
from django.db.models import ManyToManyField, DateTimeField, BooleanField, TextField, TextChoices
from rest_framework.fields import CharField

from apps.common.models import TimeStampedModel


class ProjectStatusChoice(TextChoices):
    WAITING = "waiting"
    PROGRESS = "progress"
    FINISHED = "finished"


class Project(TimeStampedModel):
    name = CharField(max_length=128)
    decription = TextField()
    employess = ManyToManyField('employee.Employee', 'employees', null=True, blank=True)
    status = CharField(max_length=255, choices=ProjectStatusChoice.choices, default=ProjectStatusChoice.WAITING)
    deadline = DateTimeField()
