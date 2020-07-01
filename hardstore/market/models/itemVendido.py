from .producto import Producto
from .orden import Orden
from django.db import models

class ItemVendido(models.Model):

    producto = models.ForeignKey(Producto, null=True, on_delete=models.CASCADE)

    orden = models.ForeignKey(Orden, null=True, on_delete=models.CASCADE)
