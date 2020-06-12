"""hardstore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
# traigo las vistas de usuarios, mas directo -Joma
from users import views as user_views
from market import views as market_views

from django.conf.urls.static import static 
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', market_views.VistaHome.as_view(), name='home'),
    
    # path('', include('market.urls')), manera menos directa -Joma
    path('login/', user_views.VistaLogin.as_view(), name='login'),
    path('signup/', user_views.VistaSignup.as_view(), name='signup'),
  
    # path para un prodcuto en particular DEL LADO DEL CLIENTE, un path dinamico 
    #path('producto/<int:pk_producto>/', market_views.VistaUnProducto.as_view(), name='producto'),

    path('producto/<int:pk_producto>/', market_views.ProductoDetail.as_view(), name='producto-detalle'),

    path('productos_categoria/<int:pk_categoria>', market_views.ProductosCategoriaList.as_view(), name='productos-categoria-list'),



    #PATH CRUD hay que pasarlo cuando creemos todo la parte de administradores
    #crear un producto
    path('crear_producto/', market_views.ProductoCreate.as_view() , name='crear_producto'),

    #modificar un producto
    path('modificar_producto/<int:id>/', market_views.VistaCRUDProducto.ModProducto , name='modificar_producto'),

    #eliminar un producto
    path('eliminar_producto/<int:id>/', market_views.VistaCRUDProducto.EliminarProducto , name='eliminar_producto'),

    #PATH CRUD para Categorias

    #crear una Categoria
    path('crear_categoria/', market_views.CategoriaCreate.as_view() , name='crear_categoria'),

    #modificar un Categoria
    path('modificar_categoria/<int:pk>/', market_views.CategoriaUpdate.as_view() , name='modificar_categoria'),

    #eliminar un Categoria
    path('eliminar_categoria/<int:pk>/', market_views.CategoriaDelete.as_view() , name='eliminar_categoria'),

]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)