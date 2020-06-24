from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpRequest
from django.forms import inlineformset_factory
from django.views.generic import View, ListView, TemplateView, CreateView, UpdateView, DeleteView, DetailView
from django.db.models import Q
from .models import Categoria,Producto,Orden,ImagenProducto
from .forms import ProductoForm,CategoriaForm,ImagenForm

# PARA PERMISOS EN VISTAS BASADAS EN CLASES
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin

class CarritoView(TemplateView):
	template_name = 'market/carrito.html'

class CompraView(TemplateView):
		template_name = 'market/compra_concretada.html'

class index(TemplateView):
    template_name = 'home.html'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)

        if(Producto.objects.count()>=3):
            context['productos'] = Producto.objects.all()[:3]
            context['hayProductos'] = True
        else:
            context['hayProductos'] = False

        if(Categoria.objects.count()>0):
            context['categorias'] = Categoria.objects.all()
            context['hayCategorias'] = True
        else:
            context['hayCategorias'] = False

        return context


class SearchView(ListView):
    model = Producto
    template_name = 'market/producto_search_list.html'
    context_object_name = 'productosList'

    def get(self,request,*args,**kwargs):
        self.nombre = self.request.GET.get('nombre')
        self.categoria = self.request.GET.get('categoria')
        self.descripcion = self.request.GET.get('descripcion')
        self.precio = self.request.GET.get('precio')
        return super().get(request,*args,**kwargs)


    def get_queryset(self):
        resultado = Producto.objects.all()
        if self.nombre:
            resultado = resultado.filter(nombre__icontains=self.nombre)
        if self.categoria:
            resultado = resultado.filter(
                categoria__nombre__icontains=self.categoria)
        if self.descripcion:
            resultado = resultado.filter(
                descripcion__icontains=self.descripcion)
        if self.precio:
            resultado = resultado.filter(precio__lte=self.precio)
        return resultado

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        if(Categoria.objects.count()>0):
            context['categorias'] = Categoria.objects.all()
            context['hayCategorias'] = True
        else:
            context['hayCategorias'] = False
        return context


class ProductosCategoriaList(ListView):
    model = Producto
    template_name = 'market/producto_categoria_list.html'
    context_object_name = 'productosList'  # para el for

    def get_queryset(self):
        self.pk_categoria = get_object_or_404(
            Categoria, id=self.kwargs['pk_categoria'])
        return Producto.productos.categorias(self.pk_categoria)

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        if(Categoria.objects.count()>0):
            context['categorias'] = Categoria.objects.all()
            context['hayCategorias'] = True
        else:
            context['hayCategorias'] = False
        return context

# https://docs.djangoproject.com/en/3.0/topics/class-based-views/generic-display/#generic-views-of-objects FILTRADO DINAMICO
# https://stackoverflow.com/questions/36950416/when-to-use-get-get-queryset-get-context-data-in-django


class ProductoDetail(DetailView):

    model = Producto

    def get_object(self):
        pk_producto = self.kwargs.get("pk_producto")
        return get_object_or_404(Producto, id=pk_producto)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        if(Categoria.objects.count()>0):
            context['categorias'] = Categoria.objects.all()
            context['hayCategorias'] = True
        else:
            context['hayCategorias'] = False
        return context


#--------------ADMINISTRACION--------------#

class ProductoCreate(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    login_url = 'login'

    success_url = '/'
    model = Producto
    form_class = ProductoForm

    def test_func(self):
        return (self.request.user.is_managerUser) or (self.request.user.is_executiveUser)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        ImagenFormset = inlineformset_factory( Producto, ImagenProducto, ImagenForm, extra=2)
        formset = ImagenFormset(queryset=ImagenProducto.objects.none())
        context['imagenes'] = formset
        return context

    def post(self, request):
        # Almacena el producto por más que los archivos cargados sean inválidos.
        super().post(request)
        ImagenFormset = inlineformset_factory(
            Producto, ImagenProducto, ImagenForm, extra=2)
        formset = ImagenFormset(request.POST or None,
                                request.FILES or None, instance=self.object)
        if formset.is_valid():
            formset.save()
            return redirect('/')


class ProductoUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    login_url = 'login'
    model = Producto
    form_class = ProductoForm
    success_url = '/'

    def test_func(self):
        return (self.request.user.is_managerUser) or (self.request.user.is_executiveUser)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        ImagenFormset = inlineformset_factory(
            Producto, ImagenProducto, ImagenForm, extra=2)
        formset = ImagenFormset(instance=self.object)
        context['imagenes'] = formset
        return context

    def post(self, request, **kwargs):
        super().post(request, **kwargs)
        ImagenFormset = inlineformset_factory(
            Producto, ImagenProducto, ImagenForm, extra=2)
        formset = ImagenFormset(request.POST or None,
                                request.FILES or None, instance=self.object)
        if formset.is_valid():
            formset.save()
            return redirect('/')


class ProductoDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    login_url = 'login'
    model = Producto
    form_class = ProductoForm
    success_url = '/'

    def test_func(self):
        return (self.request.user.is_managerUser) or (self.request.user.is_executiveUser)


class CategoriaCreate(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    login_url = 'login'
    model = Categoria
    form_class = CategoriaForm
    success_url = "/"

    def test_func(self):
        return (self.request.user.is_managerUser) or (self.request.user.is_executiveUser)


class CategoriaUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    login_url = 'login'
    model = Categoria
    form_class = CategoriaForm
    success_url = "/"

    def test_func(self):
        return (self.request.user.is_managerUser) or (self.request.user.is_executiveUser)


class CategoriaDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    login_url = 'login'
    model = Categoria
    form_class = CategoriaForm
    success_url = "/"

    def test_func(self):
        return (self.request.user.is_managerUser) or (self.request.user.is_executiveUser)
