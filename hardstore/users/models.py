from django.db import models
from django.utils import timezone


from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    is_commonUser = models.BooleanField(default=False)
    is_managerUser = models.BooleanField(default=False)  # gestor
    is_executiveUser = models.BooleanField(default=False)  # gerente
