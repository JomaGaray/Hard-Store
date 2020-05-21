from django.shortcuts import render
from django.http import HttpResponse,HttpRequest
from .models import Category,Product,Order,Customer
from django.views import View
import datetime

class VistaHome(View):
	def get(self,request):
		products = Product.objects.all()
		#ofertas = Oferta.objects.filter()
		# por ahora los destacados van a ser los productos cargados mas recientemente
		#destacados = Product.objects.filter()
		
		context = {
		'titulo':'Home',
		'products' : products#,
		#'ofertas' : ofertas ,  # hago una query de 6 productos en oferta
		#'destacados' : destacados  # hago una query de los 6 mas destacados
		}
		return render(request, 'home.html', context)
	
