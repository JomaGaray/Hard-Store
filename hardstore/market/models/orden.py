from django.db import models
from django.utils import timezone
from users.models import CustomUser


class Orden(models.Model):
    ESTADO = (	('Pendiente', 'Pendiente'),
               ('Confirmada', 'Confirmada'))

    estado = models.CharField(max_length=200, null=True, choices=ESTADO)
    f_creacion = models.DateTimeField(auto_now_add=True, null=True)

    usuario = models.ForeignKey(CustomUser, null=True, on_delete=models.CASCADE)