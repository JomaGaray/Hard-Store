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

#vista para muchos productos de una categoria en particular 
class VistaMuchosProductos(View):
	def get(self,request):
		#paso una lista de productos 
		#renderizando los datos al template
		productos= Producto.objects.all()
		
		context={
			'productos':productos,
		}
		
		return render(request, 'producto.html', context)

#vista para un producto en particular

class VistaUnProducto(View):
	def get(self,request, pk_producto):
		#url dinamico, solo busco un producto en particular 
		producto= Producto.objects.get(id = pk_producto)
		
		context={
			'producto':producto,
		}
		
		return render(request, 'producto.html', context)
