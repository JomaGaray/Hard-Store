from django.shortcuts import redirect
from django.urls import reverse

from django.views.generic import View, DeleteView

from market.models import Producto, Orden, ItemVendido

from django.contrib.auth.mixins import  LoginRequiredMixin
from django.contrib.auth.decorators import login_required

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