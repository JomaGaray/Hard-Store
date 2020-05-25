from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
#from market.models import Producto

#class Favorito(models.Model):
#	referencia a un producto
#   
#	def __str__(self):
#		return self.producto.nombre

class Cliente(models.Model):
	usuario = models.OneToOneField(User , null = True , on_delete = models.CASCADE)
	f_creacion = models.DateTimeField(auto_now_add = True ,null = True)
	#favorito = models.ForeignKey(Favorito, null=True, on_delete = models.CASCADE)

	def __str__(self):
		return self.usuario.first_name +' '+ self.usuario.last_name