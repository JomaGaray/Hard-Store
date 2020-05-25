from django.db import models
from django.utils import timezone
from users.models import Cliente
#class Image(models.Model):
#class Like(models.Model):
#class Cart(models.Model):
#class (models.Model):
#class (models.Model):

class Categoria(models.Model):
	nombre = models.CharField(max_length=200, null=True)

	def __str__(self):
		return self.nombre

class ProductoManager(models.Manager):
	def crear_producto(self,nombre,descripcion,precio,categoria):
		producto = self.create(nombre=nombre,descripcion=descripcion,precio=precio)
		return producto

class Producto(models.Model):
	nombre = models.CharField(max_length=200, null=True)
	descripcion = models.CharField(max_length=200, null=True, blank=True)
	precio = models.FloatField(null=True)
	f_creacion = models.DateTimeField(auto_now_add=True, null=True)
	categoria = models.ForeignKey(Categoria, null=True, on_delete = models.SET_NULL)
	#img_productos es un directorio que contendrá todas las images
	imagen = models.ImageField(default='default.jpg',upload_to='img_productos') 

	objects = ProductoManager()

	def __str__(self):
		return self.nombre

class Oferta(models.Model):
	producto = models.ForeignKey(Producto, null=True, on_delete = models.SET_NULL)
	descuento = models.FloatField(null=True)
	#precio = producto.precio * discount  ----- tengo que almacenar el precio con el descuento aplicado
	f_creacion = models.DateTimeField(auto_now_add=True, null=True)
	f_expira = models.DateTimeField(null=True)

	def __str__(self):
		return self.producto.nombre


class Orden(models.Model):
	ESTADO = (	('Pendiente','Pendiente'),
				('Confirmada','Confirmada'),
				('Cancelada','Cancelada')
		)
	#referencia a Producto
	producto = models.ForeignKey(Producto, null=True, on_delete = models.SET_NULL)
	#referencia a cliente
	cliente = models.ForeignKey(Cliente, null=True, on_delete = models.SET_NULL)

	estado = models.CharField(max_length=200, null=True, choices=ESTADO)

