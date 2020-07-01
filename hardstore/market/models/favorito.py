from django.db import models

from .producto import Producto
from users.models import CustomUser

class Favorito(models.Model):

    producto = models.ForeignKey(Producto, null=True, on_delete=models.CASCADE)

    usuario = models.ForeignKey(CustomUser, null=True, on_delete=models.CASCADE)