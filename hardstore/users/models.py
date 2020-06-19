from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(
        User, null=True, on_delete=models.CASCADE, related_name='profile')
    f_creacion = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return str(self.first_name)


class AdminProfile(models.Model):
    user = models.OneToOneField(
        User, null=True, on_delete=models.CASCADE)
    f_creacion = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        permissions = [
            ("crear_producto", "Puede crear un producto"),
            ("modificar_producto", "Puede modificar un producto"),
            ("eliminar_producto", "Puede eliminar un producto"),
        ]

    def __str__(self):
        return str(self.first_name)
