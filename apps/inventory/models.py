from django.db import models
from django.db.models import Model, CharField, TextField, ForeignKey, CASCADE

from apps.common.models import TimeStampedModel


class Inventory(TimeStampedModel):
    name = CharField(max_length=255)
    description = CharField(max_length=255)

    class Meta:
        db_table = 'invetory'

    def __str__(self):
        return self.name


class Product(TimeStampedModel):
    name = CharField(max_length=128)
    description = TextField()
    inventory = ForeignKey('inventory.Inventory', CASCADE, 'products')

    class Meta:
        db_table = 'product'

    def __str__(self):
        return self.name
