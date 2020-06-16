from django.db import models
from django.utils import timezone
from users.models import UserProfile

#### 	Modelo Categoria 	####

class Categoria(models.Model):
    nombre = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.nombre


#### Queryset personalizadas para ProductoManager ####
class ProductoQuerySet(models.QuerySet):
	def categorias(self,categoria):
		return self.filter(categoria = categoria)

	def producto(self,pk_producto):
		return self.get(id = pk_producto)

#### Manager personalizado para PRODUCTO ####
class ProductoManager(models.Manager):
	def get_queryset(self):		
		return ProductoQuerySet(self.model, using=self._db)
	
	def categorias(self,categoria):
		return self.get_queryset().categorias(categoria)

	def producto(self,pk_producto):
		return self.get_queryset().producto(pk_producto)


class Producto(models.Model):
    nombre = models.CharField(max_length=200, null=True)
    descripcion = models.CharField(max_length=200, null=True, blank=True)
    precio = models.FloatField(null=True)
    f_creacion = models.DateTimeField(auto_now_add=True, null=True)
    categoria = models.ForeignKey(
        Categoria, null=True, on_delete=models.SET_NULL)

	objects = models.Manager() # manager default
 
	productos = ProductoManager() # un manager personalizado

	def __str__(self):
		return self.nombre

#### 	Modelo Imagen	 ####		
class ImagenProducto(models.Model):
	producto = models.ForeignKey(Producto, on_delete = models.CASCADE)
	imagen = models.ImageField(default='default.jpg') 

	def __str__(self):
		return str(self.producto.id)

class Oferta(models.Model):
	producto = models.ForeignKey(Producto, null=True, on_delete = models.SET_NULL)
	descuento = models.FloatField(null=True) 
	f_creacion = models.DateTimeField(auto_now_add=True, null=True)
	f_expira = models.DateTimeField(null=True)

	def __str__(self):
		return str(self.producto.id)

	#def __str__(self):
	#	return self.producto.nombre

#####	MODELOS DE Favorito	 	####

class Favorito(models.Model):

	producto = models.ForeignKey(Producto, null=True, on_delete = models.CASCADE)

	cliente = models.ForeignKey(Cliente, null=True, on_delete = models.CASCADE)


####	MODELOS DE ORDEN 	#### 


# Representaria directamente el carrito / productos sin confirmar
class Orden(models.Model):
	ESTADO = (	('Pendiente','Pendiente'),
				('Confirmada','Confirmada') )

	estado = models.CharField(max_length=200, null=True, choices=ESTADO)
	f_creacion = models.DateTimeField(auto_now_add=True, null=True)
	
	#referencia a Cliente
	cliente = models.ForeignKey(Cliente, null=True, on_delete = models.CASCADE)

####	MODELOS DE ITEM VENDIDO 	#### 

# representa el posible producto a ser comprado al crearse la orden
# Y el producto comprado/vendido

class ItemVendido(models.Model):
	#fijar el precio de la compra
	#precio = models.FloatField(null=True)
	#fijar la fecha de la compra
	#f_creacion = models.DateTimeField(auto_now_add=True, null=True)

	producto = models.ForeignKey(Producto, null=True, on_delete = models.CASCADE)

	orden = models.ForeignKey(Orden, null=True, on_delete = models.CASCADE)
