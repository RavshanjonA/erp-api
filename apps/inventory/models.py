from django.db import models
from django.db.models import Model, CharField, TextField

from apps.common.models import TimeStampedModel


class Inventory(TimeStampedModel):
    name = CharField(max_length=255)
    description = CharField(max_length=255)

class Product(TimeStampedModel):
    name = CharField(max_length=128)
    description = TextField()

