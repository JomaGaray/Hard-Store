from market.models import Categoria, Producto
from django.views.generic import TemplateView

class index(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if(Producto.objects.count() >= 3):
            context['destacados'] = Producto.productos.random()[:3]
            context['productosList'] = Producto.productos.random().all()[:12]
            context['hayProductos'] = True
        else:
            context['hayProductos'] = False

        if(Categoria.objects.count() > 0):
            context['categorias'] = Categoria.objects.all()
            context['hayCategorias'] = True
        else:
            context['hayCategorias'] = False

        return context