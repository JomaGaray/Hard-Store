from django.shortcuts import render, get_object_or_404, redirect

from django.urls import reverse

from django.views.generic import ListView,  DetailView, UpdateView, CreateView, DeleteView

from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin

from market.models import Categoria, Producto, ImagenProducto

from django.forms import inlineformset_factory

from market.forms import ProductoForm, ImagenForm


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

# Listado de productos por categoría para Clienete
class ProductosCategoriaList(ListView):
    model = Producto
    template_name = 'market/producto_categoria_list.html'
    context_object_name = 'productosList'  # para el for

    def get_queryset(self):
        if(self.kwargs):
            self.pk_categoria = get_object_or_404(Categoria, id=self.kwargs['pk_categoria'])
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

# Listado de productos por categoría para Administración de productos
class ProductosListCat(ListView):
    model = Producto
    template_name = 'market/producto_list.html'
    context_object_name = 'productosList'  # para el for

    def get_queryset(self):
        return Producto.productos.categorias(self.kwargs['pk_categoria'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if(Categoria.objects.count() > 0):
            context['categorias'] = Categoria.objects.all()
            context['hayCategorias'] = True
        else:
            context['hayCategorias'] = False
        return context

# Listado de productos para Administración de productos
class ProductosList(ListView):
    model = Producto
    template_name = 'market/producto_list.html'
    context_object_name = 'productosList'  # para el for

    def get_queryset(self):
        return Producto.objects.order_by('categoria')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if(Categoria.objects.count() > 0):
            context['categorias'] = Categoria.objects.all()
            context['hayCategorias'] = True
        else:
            context['hayCategorias'] = False
        return context



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