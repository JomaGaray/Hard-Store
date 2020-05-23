from django.shortcuts import render
from django.http import HttpResponse,HttpRequest
from .models import Categoria,Producto,Orden,Cliente,Oferta
from django.views import View


class VistaHome(View):
	def get(self,request):
		productos = Producto.objects.all()
		ofertas = Oferta.objects.all()[:6] #tengo que filtrar 6 ofertas

		# por ahora los destacados van a ser los productos cargados mas recientemente
		# hago una query de los 6 mas destacados
		
		destacados = Producto.objects.all()[:6]

		
		context = {
		'titulo':'Home',
		'productos' : productos,
		'ofertas' : ofertas ,
		'destacados' : destacados  
		}
		return render(request, 'home.html', context)
	
class VistaProducto(View):
	def get(self,request):
		return render(request, 'producto.html')
