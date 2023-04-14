from django.db import models
from django.db.models import Model, TextField, DateTimeField
from rest_framework.fields import CharField


class Event(Model):
    name = CharField(max_length=128)
    decription = TextField()
    datetime = DateTimeField()


