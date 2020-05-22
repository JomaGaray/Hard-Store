from django.shortcuts import render
from django.http import HttpResponse,HttpRequest
from .models import Categoria,Producto,Orden,Cliente,Oferta
from django.views import View


class VistaHome(View):
	def get(self,request):
		productos = Producto.objects.all()
		ofertas = Oferta.objects.all() #tengo que filtrar 6 ofertas

		# por ahora los destacados van a ser los productos cargados mas recientemente
		# hago una query de los 6 mas destacados
		
		#destacados = Product.objects.filter()

		
		context = {
		'titulo':'Home',
		'productos' : productos,
		'ofertas' : ofertas 
		#'destacados' : destacados  
		}
		return render(request, 'home.html', context)
	
