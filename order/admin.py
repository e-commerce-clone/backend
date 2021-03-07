from django.contrib import admin
from .models import Order_item, Order
# Register your models here.

admin.site.register(Order)
admin.site.register(Order_item)
