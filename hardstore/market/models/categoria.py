from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.nombre