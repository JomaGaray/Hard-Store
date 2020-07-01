from django.shortcuts import  redirect

from django.http import  HttpResponseRedirect

from django.urls import reverse

from django.views.generic import View, ListView, DeleteView


from market.models import Categoria, Producto, Favorito

# PARA PERMISOS EN VISTAS BASADAS EN CLASES
from django.contrib.auth.mixins import  LoginRequiredMixin

from django.contrib.auth.decorators import login_required


class LikeProduct(LoginRequiredMixin, View):
    login_url = 'login'

    def get(self, request, pk_producto):
        producto = Producto.objects.get(id=pk_producto)
        favorito, created = Favorito.objects.get_or_create(
            usuario=request.user, producto=producto)
        # redirijo a la misma pagina del producto
        return HttpResponseRedirect(reverse('producto-detalle', args=[str(pk_producto)]))

class LikeDelete(LoginRequiredMixin, DeleteView):
    login_url = 'login'
    model = Favorito
    success_url = "/"

    def post(self,request,**kwargs):
        super().post(request, **kwargs)
        return redirect(reverse('LikeList'))    

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