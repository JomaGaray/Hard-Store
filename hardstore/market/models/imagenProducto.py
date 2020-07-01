from django.db import models
from .producto import Producto
from django.utils import timezone
from users.models import CustomUser

class ImagenProducto(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    imagen = models.ImageField(default='default.jpg')

    def __str__(self):
        return str(self.producto.id)