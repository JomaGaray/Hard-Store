from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse,HttpRequest
from .models import Categoria,Producto,Orden,Cliente,Oferta,ImagenProducto
from .forms import ProductoForm,CategoriaForm,ImagenForm
from django.forms import inlineformset_factory
from django.views.generic import View,ListView,TemplateView,CreateView,UpdateView,DeleteView,DetailView


class index(TemplateView):
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

class ProductosCategoriaList(ListView):
    model = Producto
    context_object_name = 'productosList'  # para el for

    def get_queryset(self):
        self.pk_categoria = get_object_or_404(
            Categoria, id=self.kwargs['pk_categoria'])
        return Producto.productos.categorias(self.pk_categoria)

# https://docs.djangoproject.com/en/3.0/topics/class-based-views/generic-display/#generic-views-of-objects FILTRADO DINAMICO
# https://stackoverflow.com/questions/36950416/when-to-use-get-get-queryset-get-context-data-in-django

class ProductoDetail(DetailView):
	
	model = Producto
	
	def get_object(self):
		pk_producto = self.kwargs.get("pk_producto")
		return get_object_or_404(Producto,id=pk_producto)


#################### VISTAS CRUD PRODUCTO-IMAGENES ########################

#ESTA VISTA DEBE SER IMPLEMENTADA SOLAMENTE PARA LOS ADMINISTRADORES

class ProductoCreate(CreateView):

	success_url = '/'
	model = Producto
	form_class = ProductoForm

	def get_context_data(self,**kwargs):
		context = super().get_context_data(**kwargs)
		ImagenFormset = inlineformset_factory(Producto, ImagenProducto, ImagenForm , extra = 2)
		formset = ImagenFormset(queryset = ImagenProducto.objects.none())
		context['imagenes'] = formset
		return context 

	def post(self,request): 
		super().post(request)
		ImagenFormset = inlineformset_factory(Producto, ImagenProducto, ImagenForm , extra = 2)
		formset = ImagenFormset(request.POST or None, request.FILES or None, instance=self.object)
		if formset.is_valid():
			formset.save()


class ProductoUpdate(UpdateView):
	model = Producto
	form_class = ProductoForm
	success_url = '/'

	def get_context_data(self,**kwargs):
		context = super().get_context_data(**kwargs)
		ImagenFormset = inlineformset_factory(Producto, ImagenProducto, ImagenForm , extra = 2)
		formset = ImagenFormset(instance=self.object)
		context['imagenes'] = formset	
		return context 

	def post(self,request,**kwargs): 
		super().post(request,**kwargs)
		ImagenFormset = inlineformset_factory(Producto, ImagenProducto, ImagenForm , extra = 2)
		formset = ImagenFormset(request.POST or None, request.FILES or None,instance=self.object) 		
		if formset.is_valid():
			formset.save()
			return redirect('/')

class ProductoDelete(DeleteView):
		model = Producto
		form_class = ProductoForm
		success_url = '/'


class CategoriaCreate(CreateView):
	model = Categoria
	form_class = CategoriaForm
	success_url = "/"

class CategoriaUpdate(UpdateView):
	model = Categoria
	form_class = CategoriaForm
	success_url = "/"

class CategoriaDelete(DeleteView):
	model = Categoria
	form_class = CategoriaForm
	success_url = "/"
