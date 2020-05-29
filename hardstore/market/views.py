from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse,HttpRequest
from .models import Categoria,Producto,Orden,Cliente,Oferta
from .forms import ProductoForm
from django.views.generic import View,ListView,TemplateView


################ VISTA DEL HOME ################

#Implementacion con TemplateView
class VistaHome(TemplateView):
	template_name = 'home.html'
	
	def get_context_data(self,**kwargs):
		context = super().get_context_data(**kwargs)
		context['productos'] = Producto.objects.all()
		context['ofertas'] = Oferta.objects.all()[:6]
		context['destacados'] = Producto.objects.all()[:6]
		context['titulo'] = 'home'
		# traigo todas las categorias
		context['categorias'] = Categoria.objects.all()
		return context



################ VISTA DE UN PRODUCTO ################

#vista para muchos productos de una categoria en particular 
class VistaMuchosProductos(ListView):
    template_name = 'productosCategoria.html'
    model = Producto
    context_object_name = 'productsList'  # para el for
#    queryset = Producto.objects.filter(categoria=self.kwargs['pk_categoria'])

    def get_queryset(self):
        self.pk_categoria = get_object_or_404(
            Categoria, id=self.kwargs['pk_categoria'])
        return Producto.objects.filter(categoria=self.pk_categoria)

# https://docs.djangoproject.com/en/3.0/topics/class-based-views/generic-display/#generic-views-of-objects FILTRADO DINAMICO
# https://stackoverflow.com/questions/36950416/when-to-use-get-get-queryset-get-context-data-in-django


################ VISTA DE UN PRODUCTO ###################

#Implementacion con TemplateView
class VistaUnProducto(TemplateView):
	template_name = 'producto.html'
	
	def get_context_data(self,**kwargs):
		context = super().get_context_data(**kwargs) #obtiene los datos del modelo, en este caso "Producto"
		pk_producto = kwargs['pk_producto'] #tomo el argumento del url que indica el numero id del producto
		context['producto'] = Producto.objects.get(id = pk_producto) #añado otro field al modelo
								#y le asigno una queryset para que seleccione el producto especifico 
		return context


#################### VISTA CREATE,READ,UPDATE,DELETE ########################

#ESTA VISTA DEBE SER IMPLEMENTADA SOLAMENTE PARA LOS ADMINISTRADORES

class VistaCRUDProducto(View):

	def CrearProducto(request):
		form = ProductoForm()
		if request.method == 'POST':
			form = ProductoForm(request.POST)
			if form.is_valid():
				form.save()
				# post.user = request.user - A futuro para saber que administrador realizo esta accion
				return redirect('/') #redirecciona a la lista de productos
		return render(request,'producto_form.html',{'producto':form})

	def ModProducto(request,id):
		producto = get_object_or_404(Producto,pk=id)
		form = ProductoForm(instance=producto)
		if request.method == 'POST':
			form = ProductoForm(request.POST, request.FILES, instance=producto) #request.FILES es debido a las imagenes
			if form.is_valid():
				form.save()
				return redirect('/') #redirecciona a la lista de productos
		return render(request,'producto_form.html',{'producto':form})

	def EliminarProducto(request,id):
		#Producto.objecets.filter(pk=id).delete()
		producto = get_object_or_404(Producto,pk=id)
		if request.method == 'POST':
			producto.delete()
			return redirect('/') #redirecciona a la lista de productos
		args = {'producto':producto}
		# redirecciona a una lista de productos que NO va a ser la misma de los clientes
		return render(request, 'eliminar_producto.html' , args)