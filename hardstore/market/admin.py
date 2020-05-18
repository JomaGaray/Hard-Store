from django.contrib import admin
from django.contrib.auth.admin import Group
from .models import Product,Customer,Order,Category

admin.site.unregister(Group)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Category)