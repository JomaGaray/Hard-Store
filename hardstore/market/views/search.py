from market.models import Categoria, Producto
from django.views.generic import ListView

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
        context['nombre'] = self.nombre 
        context['categoria'] = self.categoria 
        context['descripcion'] = self.descripcion
        context['precio'] = self.precio
        if(Categoria.objects.count() > 0):
            context['categorias'] = Categoria.objects.all()
            context['hayCategorias'] = True
        else:
            context['hayCategorias'] = False
        return context
