from django.contrib import admin
from django.contrib.auth.admin import Group
from .models import Producto,Orden,Categoria

admin.site.unregister(Group)
admin.site.register(Producto)
admin.site.register(Orden)
admin.site.register(Categoria)
