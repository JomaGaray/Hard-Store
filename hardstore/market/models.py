from django.db import models
from django.utils import timezone
from users.models import UserProfile


class Categoria(models.Model):
    nombre = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.nombre


class ProductoManager(models.Manager):
    def crear_producto(self, nombre, descripcion, precio, categoria):
        producto = self.create(
            nombre=nombre, descripcion=descripcion, precio=precio)
        return producto


class Producto(models.Model):
    nombre = models.CharField(max_length=200, null=True)
    descripcion = models.CharField(max_length=200, null=True, blank=True)
    precio = models.FloatField(null=True)
    f_creacion = models.DateTimeField(auto_now_add=True, null=True)
    categoria = models.ForeignKey(
        Categoria, null=True, on_delete=models.SET_NULL)

    # img_productos es un directorio que contendrá todas las images

    # es necesario un modelo imagen que solo contenga esta relación -----------------------------------= ?????

    imagen = models.ImageField(null=True, default='default.jpg')

    objects = ProductoManager()

    def __str__(self):
        return self.nombre


class Oferta(models.Model):
    producto = models.ForeignKey(
        Producto, null=True, on_delete=models.SET_NULL)
    # que tipo de Field debe ser un descuento -----------------= ?????
    descuento = models.FloatField(null=True)
    f_creacion = models.DateTimeField(auto_now_add=True, null=True)
    f_expira = models.DateTimeField(null=True)

    # def __str__(self):
    #	return self.producto.nombre

# class Compra(models.Model):
#	#representa la lista de una o mas ordenes confirmadas, es decir productos vendidos
#
#	cliente = models.ForeignKey(Cliente, null=True, on_delete = models.CASCADE)
#
#	#las ordenes confirmadas referencian a este modelo

# MODELOS DE ORDEN 	#### -----------------------------------------------------------------------= ?????

# Primer Modelo de Orden

# La misma orden define si esta pendiente o confirmada(vendida)

# El carrito solo contendrá las pendientes


class Orden(models.Model):
    ESTADO = (	('Pendiente', 'Pendiente'),
               ('Confirmada', 'Confirmada'),
               # ('Cancelada','Cancelada') que la orden este cancelada implica la inesistencia de la relacion ---------= ?????
               )
    # referencia a Producto
    producto = models.ForeignKey(Producto, null=True, on_delete=models.CASCADE)
    # referencia a cliente
    UserProfile = models.ForeignKey(
        UserProfile, null=True, on_delete=models.CASCADE)
    estado = models.CharField(max_length=200, null=True, choices=ESTADO)

# Segunda opcion de Modelo de Ordenes

# Se dividen las ordenes por su estado y creo un modelo Compra que contiene todos las ordenes confirmadas

# El carrito solo contendrá las pendientes al igual que el anterior esquema

#	 class Orden(models.Model):
#		referencia a Producto
#		producto = models.ForeignKey(Producto, null=True, on_delete = models.CASCADE)

# Si sigo este criterio las demas ordenes heredaran de este modelo

#	class OrdenPendiente(models.Model):
#
#		#referencia a Producto
#		producto = models.ForeignKey(Producto, null=True, on_delete = models.CASCADE)
#		#referencia a carrito
#	 	carrito = models.ForeignKey(Carrito, null=True, on_delete = models.CASCADE)
#
#	class OrdenConfirmada(models.Model):
#
#		#referencia a Producto
#		producto = models.ForeignKey(Producto, null=True, on_delete = models.CASCADE)
#		#referencia a compra
#	 	compra = models.ForeignKey(Carrito, null=True, on_delete = models.CASCADE)


# MODELOS DE CARRITO 	#### -----------------------------------------------------------------------= ?????

# Primer Modelo de Carrito

# El carrito contendra solo ordenes pendientes  -------------------------------------------------------------= ?????
# class Carrito(models.Model):
#	# representa la lista de una o mas ordenes pendientes, es decir productos a vender
#
#	#referencia a un cliente
#	cliente = models.OneToOneField(Cliente , null = True , on_delete = models.CASCADE)
#
#
# Puede ser representado como la lista de ordenes que posee el cliente


#####	MODELOS DE Favorito	 	####
#
# Primer Modelo de Favorito
#
# class Favorito(models.Model):
#
#	producto = models.ForeignKey(Producto, null=True, on_delete = models.CASCADE)
#
#	cliente = models.ForeignKey(Cliente, null=True, on_delete = models.CASCADE)
