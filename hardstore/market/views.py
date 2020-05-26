from django.shortcuts import render
from django.http import HttpResponse,HttpRequest
from .models import Categoria,Producto,Orden,Cliente,Oferta
from django.views.generic import View,ListView,TemplateView

#Implementacion con TemplateView
class VistaHome(TemplateView):
	template_name = 'home.html'
	
	def get_context_data(self,**kwargs):
		context = super().get_context_data(**kwargs)
		context['productos'] = Producto.objects.all()
		context['ofertas'] = Oferta.objects.all()[:6]
		context['destacados'] = Producto.objects.all()[:6]
		context['titulo'] = 'home'
		return context

#Implementacion anterior
#class VistaHome(View):
#	def get(self,request):
#		productos = Producto.objects.all()
#		ofertas = Oferta.objects.all()[:6] #tengo que filtrar 6 ofertas
#
#		# por ahora los destacados van a ser los productos cargados mas recientemente
#		# hago una query de los 6 mas destacados
#		
#		destacados = Producto.objects.all()[:6]
#
#		
#		context = {
#		'titulo':'Home',
#		'productos' : productos,
#		'ofertas' : ofertas ,
#		'destacados' : destacados  
#		}
#		return render(request, 'home.html', context)

#vista para muchos productos de una categoria en particular 
class VistaMuchosProductos(View): #se comporta como una ListView
	def get(self,request):
		productos= Producto.objects.all()
		
		context={
			'productos':productos,
		}
		
		return render(request, 'producto.html', context)
#Implementacion vistaMuchosProductos con ListView
#class ProductosList(ListView)
#	template_name = 'abc.html'
#	model = Producto
#	context_object_name = 'productos'
#
#	el url que hace referencia a una categoria contendra dinamicamente el nombre
#   traera el nombre como parametro y poder asi realizar la queryset filtrado por esa categoria
# y devolver el template con la lista


#Implementacion con TemplateView
class VistaUnProducto(TemplateView):
	template_name = 'producto.html'
	
	def get_context_data(self,**kwargs):
		context = super().get_context_data(**kwargs) #obtiene los datos del modelo, en este caso "Producto"
		pk_producto = kwargs['pk_producto'] #tomo el argumento del url que indica el numero id del producto
		context['producto'] = Producto.objects.get(id = pk_producto) #añado otro field al modelo
								#y le asigno una queryset para que seleccione el producto especifico 
		return context

#Implementacion anterior	
#class VistaUnProducto(View):
#	def get(self,request, pk_producto):
#		#url dinamico, solo busco un producto en particular 
#		producto= Producto.objects.get(id = pk_producto)
#		
#		context={
#			'producto':producto,
#		}
#		
#		return render(request, 'producto.html', context)