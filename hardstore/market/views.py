from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse,HttpRequest
from .models import Categoria,Producto,Orden,Cliente,Oferta,ImagenProducto
from .forms import ProductoForm,CategoriaForm,ImagenForm
from django.forms import modelformset_factory,inlineformset_factory
from django.views.generic import View,ListView,TemplateView,CreateView,UpdateView,DeleteView,DetailView



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
class ProductosCategoriaList(ListView):
#	template_name = 'productosCategoria.html'
    model = Producto
    context_object_name = 'productosList'  # para el for
#   queryset = Producto.objects.filter(categoria=self.kwargs['pk_categoria'])

    def get_queryset(self):
        self.pk_categoria = get_object_or_404(
            Categoria, id=self.kwargs['pk_categoria'])
        return Producto.productos.categorias(self.pk_categoria)

# https://docs.djangoproject.com/en/3.0/topics/class-based-views/generic-display/#generic-views-of-objects FILTRADO DINAMICO
# https://stackoverflow.com/questions/36950416/when-to-use-get-get-queryset-get-context-data-in-django


################ VISTA DE UN PRODUCTO ###################

#Implementacion con TemplateView
#class VistaUnProducto(TemplateView):
#	template_name = 'producto.html'
#	
#	def get_context_data(self,**kwargs):
#		context = super().get_context_data(**kwargs) #obtiene los datos del modelo, en este caso "Producto"
#		pk_producto = kwargs['pk_producto'] #tomo el argumento del url que indica el numero id del producto
#		context['producto'] = Producto.productos.producto(pk_producto) #añado otro field al modelo
#								#y le asigno una queryset para que seleccione el producto especifico 
#		return context

class ProductoDetail(DetailView):
	#template_name = 'producto.html' DetailView por defecto utilzia el prefijo 'modelo_detail.html' para redireccionar al template
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
			return redirect('/') 

#class ProductoCreate(CreateView):
#
#	template_name = 'producto_form.html' 
#	success_url = '/'
#	model = Producto
#	form_class = ProductoForm
#
#	def get_context_data(self,**kwargs):
#		context = super().get_context_data(**kwargs)
#		form = ProductoForm()
#		ImagenFormset = inlineformset_factory(Producto, ImagenProducto, ImagenForm , extra = 2)
#		formset = ImagenFormset(queryset = ImagenProducto.objects.none())
#		context['form'] = form
#		context['imagenes'] = formset
#		
#		return context 
#
#	def post(self,request):
#		ImagenFormset = inlineformset_factory(Producto, ImagenProducto, ImagenForm , extra = 2)
#		form = ProductoForm(request.POST)
#		formset = ImagenFormset(request.POST or None, request.FILES or None, instance=form.instance)
#		if form.is_valid() and formset.is_valid():
#			form.save()
#			formset.save()
#			return redirect('/') 
	
	### consultar con matias funcion y/o necesidad de form_valid ###

	#def form_valid(self,form):
	#	form.save()
	#	return redirect(self.get_success_url())		

	#def post(self,request): # ProcessFormView - Constructs a form, checks the form for validity, and handles it accordingly.
	#	ImagenFormset = inlineformset_factory(Producto, ImagenProducto, ImagenForm , extra = 2)
	#	form = ProductoForm(request.POST)
	#	formset = ImagenFormset(request.POST or None, request.FILES or None, instance=form.instance)
	#	if form.is_valid():
	#		return self.form_valid(form)
	#	if formset.is_valid():
	#		return self.form_valid(formset)


		

	#def form_valid(self,)
	#	ImagenFormset = inlineformset_factory(Producto, ImagenProducto, ImagenForm , extra = 2)
	#	form = ProductoForm(request.POST)
	#	formset = ImagenFormset(request.POST or None, request.FILES or None, instance=form.instance)
	#	if form.is_valid() and formset.is_valid():
	#		form.save()
	#		formset.save()


class VistaCRUDProducto(View):
	
	#def CrearProducto(request):
	#	ImagenFormset = inlineformset_factory(Producto, ImagenProducto, ImagenForm , extra = 2)
	#	if request.method == 'POST':
	#		form = ProductoForm(request.POST)
	#		formset = ImagenFormset(request.POST or None, request.FILES or None, instance=form.instance)
	#		if form.is_valid() and formset.is_valid():
	#			form.save()
	#			formset.save()
	#			return redirect('/') 
	#	form = ProductoForm()
	#	formset = ImagenFormset(queryset = ImagenProducto.objects.none())
	#	context = {
	#		'form' : form,
	#		'imagenes' : formset
	#	}
	#	return render(request,'producto_form.html',context)


### TRABAJAR PODER MODIFICAR IMAGENES YA CARGADAS ####
		
	def ModProducto(request,id):
		ImagenFormset = inlineformset_factory(Producto, ImagenProducto, ImagenForm , extra = 2)

		producto = get_object_or_404(Producto,pk=id)
		form = ProductoForm(instance=producto)		
		
		if request.method == 'POST':
			form = ProductoForm(request.POST or None, instance=producto) 

			formset = ImagenFormset(request.POST or None, request.FILES or None,instance=producto) 
			
			if form.is_valid() and formset.is_valid():
				form.save()
				formset.save()

				return redirect('/') #redirecciona a la lista de productos

		formset = ImagenFormset(instance=producto)

		context = {
			'form' : form,
			'imagenes' : formset,
		}
		return render(request,'producto_form.html',context)

	def EliminarProducto(request,id):
		#Producto.objecets.filter(pk=id).delete()
		producto = get_object_or_404(Producto,pk=id)
		if request.method == 'POST':
			producto.delete()
			return redirect('/') #redirecciona a la lista de productos
		args = {'producto':producto}
		# redirecciona a una lista de productos que NO va a ser la misma de los clientes
		return render(request, 'eliminar_producto.html' , args)


class CategoriaCreate(CreateView):
	model = Categoria
	template_name = 'categoria_form.html'
	form_class = CategoriaForm
	success_url = "/"

class CategoriaUpdate(UpdateView):
	model = Categoria
	template_name = 'categoria_form.html'
	form_class = CategoriaForm

	success_url = "/"

class CategoriaDelete(DeleteView):
	model = Categoria
	template_name = 'eliminar_categoria.html'
	form_class = CategoriaForm

	success_url = "/"

#class VistaCRUDCategoria(View):

	#def CrearCategoria(request):
	#	form = CategoriaForm()
	#	if request.method == 'POST':
	#		form = CategoriaForm(request.POST)
	#		if form.is_valid():
	#			form.save()
	#			# post.user = request.user - A futuro para saber que administrador realizo esta accion
	#	return render(request,'categoria_form.html',{'categoria':form})

	#def ModCategoria(request,id):
	#	categoria = get_object_or_404(Categoria,pk=id)
	#	form = CategoriaForm(instance=categoria)
	#	if request.method == 'POST':
	#		form = CategoriaForm(request.POST, request.FILES, instance=categoria) #request.FILES es debido a las imagenes
	#		if form.is_valid():
	#			form.save()
	#	return render(request,'categoria_form.html',{'categoria':form})

	#def EliminarCategoria(request,id):
	#	#Categoria.objecets.filter(pk=id).delete()
	#	categoria = get_object_or_404(Categoria,pk=id)
	#	if request.method == 'POST':
	#		categoria.delete()
	#	form = CategoriaForm(instance=categoria)
	#	# redirecciona a una lista de productos que NO va a ser la misma de los clientes
	#	return render(request, 'eliminar_categoria.html' , form)