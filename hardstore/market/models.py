from django.db import models
from django.utils import timezone

#class Image(models.Model):
#class Like(models.Model):
#class Cart(models.Model):
#class (models.Model):
#class (models.Model):

class Category(models.Model):
	name = models.CharField(max_length=200, null=True)

	def __str__(self):
		return self.name

class Product(models.Model):
	name = models.CharField(max_length=200, null=True)
	description = models.CharField(max_length=200, null=True, blank=True)
	price = models.FloatField(null=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	category = models.ManyToManyField(Category)

	def __str__(self):
		return self.name

class Oferta(models.Model):
	product = models.ForeignKey(Product, null=True, on_delete = models.SET_NULL)
	discount = models.FloatField(null=True)
	#price = product.price * discount  ----- tengo que almacenar el precio con el descuento aplicado
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	finish_date = models.DateTimeField(null=True)

	def __str__(self):
		return self.product.name


class Customer(models.Model):
	name = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200, null=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)

	def __str__(self):
		return self.name


class Order(models.Model):
	STATUS = (	('Pendiente','Pendiente'),
				('Confirmada','Confirmada'),
				('Cancelada','Cancelada')
		)
	#referencia a product
	product = models.ForeignKey(Product, null=True, on_delete = models.SET_NULL)
	#referencia a customer
	customer = models.ForeignKey(Customer, null=True, on_delete = models.SET_NULL)

	status = models.CharField(max_length=200, null=True, choices=STATUS)

