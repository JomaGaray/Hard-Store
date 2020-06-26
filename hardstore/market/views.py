from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.urls import reverse
from django.forms import inlineformset_factory
from django.views.generic import View, ListView, TemplateView, CreateView, UpdateView, DeleteView, DetailView
from django.db.models import Q

from .models import Categoria, Producto, Orden, ImagenProducto, ItemVendido, Favorito
from .forms import ProductoForm, CategoriaForm, ImagenForm

# PARA PERMISOS EN VISTAS BASADAS EN CLASES
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.contrib.auth.decorators import login_required



class index(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if(Producto.objects.count() >= 3):
            context['productos'] = Producto.productos.random()[:3]
            context['hayProductos'] = True
        else:
            context['hayProductos'] = False

        if(Categoria.objects.count() > 0):
            context['categorias'] = Categoria.objects.all()
            context['hayCategorias'] = True
        else:
            context['hayCategorias'] = False

        return context


class SearchView(ListView):
    model = Producto
    template_name = 'market/producto_search_list.html'
    context_object_name = 'productosList'
    paginate_by = 8

    def get(self, request, *args, **kwargs):
        self.nombre = self.request.GET.get('nombre')
        self.categoria = self.request.GET.get('categoria')
        self.descripcion = self.request.GET.get('descripcion')
        self.precio = self.request.GET.get('precio')
        return super().get(request, *args, **kwargs)

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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if(Categoria.objects.count() > 0):
            context['categorias'] = Categoria.objects.all()
            context['hayCategorias'] = True
        else:
            context['hayCategorias'] = False
        return context


class ProductoDetail(DetailView):

    model = Producto

    def get_object(self):
        pk_producto = self.kwargs.get("pk_producto")
        return get_object_or_404(Producto, id=pk_producto)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if(Categoria.objects.count() > 0):
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
        if(self.kwargs):
            self.pk_categoria = get_object_or_404(
                Categoria, id=self.kwargs['pk_categoria'])
            return Producto.productos.categorias(self.pk_categoria)
        else:
            return Producto.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if(Categoria.objects.count() > 0):
            context['categorias'] = Categoria.objects.all()
            context['hayCategorias'] = True
        else:
            context['hayCategorias'] = False
        return context


class ProductosList(ListView):
    model = Producto
    template_name = 'market/producto_list.html'
    context_object_name = 'productosList'  # para el for

    def get_queryset(self):
        return Producto.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if(Categoria.objects.count() > 0):
            context['categorias'] = Categoria.objects.all()
            context['hayCategorias'] = True
        else:
            context['hayCategorias'] = False
        return context
# https://docs.djangoproject.com/en/3.0/topics/class-based-views/generic-display/#generic-views-of-objects FILTRADO DINAMICO
# https://stackoverflow.com/questions/36950416/when-to-use-get-get-queryset-get-context-data-in-django


class CategoriasList(ListView):
    model = Categoria
    template_name = 'market/categoria_list.html'
    context_object_name = 'categoriasList'

    def get_queryset(self):
        return Categoria.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if(Categoria.objects.count() > 0):
            context['categorias'] = Categoria.objects.all()
            context['hayCategorias'] = True
        else:
            context['hayCategorias'] = False
        return context


class LikeProduct(LoginRequiredMixin, View):
    login_url = 'login'

    def get(self, request, pk_producto):
        producto = Producto.objects.get(id=pk_producto)
        favorito, created = Favorito.objects.get_or_create(
            usuario=request.user, producto=producto)
        # redirijo a la misma pagina del producto
        return HttpResponseRedirect(reverse('producto-detalle', args=[str(pk_producto)]))


class LikeProductList(LoginRequiredMixin, ListView):
    login_url = 'login'
    template_name = 'market/likeList.html'
    context_object_name = 'LikeList'

    def get_queryset(self):
        favoritos = Favorito.objects.filter(
            usuario=self.request.user)  # likeados por
        return favoritos

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if(Categoria.objects.count() > 0):
            context['categorias'] = Categoria.objects.all()
            context['hayCategorias'] = True
        else:
            context['hayCategorias'] = False
        return context

class ItemCreate(LoginRequiredMixin, View):

    login_url = 'login'
    success_url = '/' 

    def get(self,request,**kwargs):
        
        producto = Producto.objects.get(id = kwargs['pk_producto'])
        # tengo que traer la ultiama orden que haya creado el usuario, las anteriores se dan a entender
        # que fueron confirmadas
        orden, created = Orden.objects.get_or_create(estado='Pendiente',usuario= request.user)
        item = ItemVendido.objects.create(producto=producto,orden=orden)
        return redirect(reverse('carrito'))

class ItemDelete(LoginRequiredMixin, DeleteView):
    login_url = 'login'
    model = ItemVendido
    success_url = "/"

    def post(self,request,**kwargs):
        super().post(request, **kwargs)
        return redirect(reverse('carrito'))    
            


class CarritoList(ListView):
    template_name = 'market/carrito.html'    
    model = ItemVendido    
    context_object_name = 'itemList'  

    def get_queryset(self):
        return ItemVendido.objects.filter(orden__usuario = self.request.user)

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        if(Categoria.objects.count()>0):
            context['categorias'] = Categoria.objects.all()
            context['hayCategorias'] = True
        else:
            context['hayCategorias'] = False

        items = ItemVendido.objects.filter(orden__usuario = self.request.user)
        total=0
        for item in items:
            total+=item.producto.precio
        context['total'] = total

        return context

class CompraView(TemplateView):
    template_name = 'market/compra_concretada.html'


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
        ImagenFormset = inlineformset_factory(
            Producto, ImagenProducto, ImagenForm, extra=2)
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
            return redirect(reverse('modificar_producto'))


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
            return redirect(reverse('modificar_producto'))


class ProductoDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    login_url = 'login'
    model = Producto
    form_class = ProductoForm
    success_url = '../../modificar_producto/'

    def test_func(self):
        return (self.request.user.is_managerUser) or (self.request.user.is_executiveUser)


class CategoriaCreate(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    login_url = 'login'
    model = Categoria
    form_class = CategoriaForm
    success_url = "/"

    def test_func(self):
        return (self.request.user.is_managerUser) or (self.request.user.is_executiveUser)

    def post(self, request, **kwargs):
        super().post(request, **kwargs)
        return redirect(reverse('modificar_categoria'))


class CategoriaUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    login_url = 'login'
    model = Categoria
    form_class = CategoriaForm
    success_url = "/"

    def post(self, request, **kwargs):
        super().post(request, **kwargs)
        return redirect(reverse('modificar_categoria'))

    def test_func(self):
        return (self.request.user.is_managerUser) or (self.request.user.is_executiveUser)


class CategoriaDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    login_url = 'login'
    model = Categoria
    form_class = CategoriaForm
    success_url = "/"

    def post(self,request,**kwargs):
        
        categoria = Producto.objects.filter(categoria=kwargs['pk'])
        if not categoria:
            super().post(request, **kwargs)
            return redirect(reverse('modificar_categoria'))
        else:  
            return redirect(reverse('modificar_producto'))
        


    def test_func(self):
        return (self.request.user.is_managerUser) or (self.request.user.is_executiveUser)
