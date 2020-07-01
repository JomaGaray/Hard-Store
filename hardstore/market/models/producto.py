from .categoria import Categoria

from django.db import models
from django.utils import timezone
from users.models import CustomUser


#### Queryset personalizadas para ProductoManager ####
class ProductoQuerySet(models.QuerySet):
    def categorias(self, categoria):
        return self.filter(categoria=categoria)

    def producto(self, pk_producto):
        return self.get(id=pk_producto)



#### Manager personalizado para PRODUCTO ####


class ProductoManager(models.Manager):
    def get_queryset(self):
        return ProductoQuerySet(self.model, using=self._db)

    def categorias(self, categoria):
        return self.get_queryset().categorias(categoria)

    def producto(self, pk_producto):
        return self.get_queryset().producto(pk_producto)

    def random(self):
        return super(ProductoManager,self).get_queryset().order_by('?')




class Producto(models.Model):
    nombre = models.CharField(max_length=200, null=True)
    descripcion = models.CharField(max_length=200, null=True, blank=True)
    precio = models.FloatField(null=True)
    f_creacion = models.DateTimeField(auto_now_add=True, null=True)
    categoria = models.ForeignKey(Categoria, null=True, on_delete=models.SET_NULL)

    objects = models.Manager()  # manager default

    productos = ProductoManager()  # un manager personalizado

    def __str__(self):
        return self.nombre

    def imagenes(self):
    	return self.imagenproducto_set.all()