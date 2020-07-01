from market.models import Categoria, ItemVendido

from django.views.generic import ListView, TemplateView

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
