from django.contrib import admin

from .models import Inventory, Product

admin.site.register([Inventory, Product])
