from django.db import models
from django.db.models import ManyToManyField, DateTimeField, CharField, TextField, TextChoices

from apps.common.models import TimeStampedModel


class ProjectStatusChoice(TextChoices):
    WAITING = "waiting"
    PROGRESS = "progress"
    FINISHED = "finished"


class Project(TimeStampedModel):
    name = CharField(max_length=128)
    decription = TextField()
    employess = ManyToManyField('employee.Employee', 'employees')
    status = CharField(max_length=128, choices=ProjectStatusChoice.choices,default=ProjectStatusChoice.WAITING)
    deadline = DateTimeField()

    def __str__(self):
        return self.name

    class Meta:
        db_table='project'