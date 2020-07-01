from django.shortcuts import redirect

from django.urls import reverse

from django.views.generic import ListView, UpdateView, CreateView, DeleteView

from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin

from market.models import Categoria, Producto

from market.forms import CategoriaForm

class CategoriasList(ListView):
    model = Categoria
    template_name = 'market/categoria_list.html'
    context_object_name = 'categoriasList'

    def get_queryset(self):
        return Categoria.objects.order_by('nombre')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if(Categoria.objects.count() > 0):
            context['categorias'] = Categoria.objects.all()
            context['hayCategorias'] = True
        else:
            context['hayCategorias'] = False
        return context


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
