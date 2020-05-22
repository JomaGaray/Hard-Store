from django.contrib import admin
from django.contrib.auth.admin import Group
from .models import Producto,Cliente,Orden,Categoria,Oferta

admin.site.unregister(Group)
admin.site.register(Producto)
admin.site.register(Orden)
admin.site.register(Categoria)
admin.site.register(Oferta)
admin.site.register(Cliente)