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
    path('', market_views.index.as_view(), name='home'),
    path('', include('users.urls')),
    

    # Busqueda de productos
    path('search/', market_views.SearchView.as_view(), name='search'),
    
    path('producto/<int:pk_producto>/',market_views.ProductoDetail.as_view(), name='producto-detalle'),
    path('productos_categoria/<int:pk_categoria>',market_views.ProductosCategoriaList.as_view(), name='productos-categoria-list'),

    

    path('carrito/', market_views.CarritoList.as_view(), name='carrito'),

    path('add-carrito/<int:pk_producto>/', market_views.ItemCreate.as_view(), name='carrito-add'),

    path('eliminar-item/<int:pk>/',market_views.ItemDelete.as_view(), name='eliminar-item'),


    path('compra_concretada/', market_views.CompraView.as_view(), name='compra_concretada'),


    # -------Administracion-------
    path('crear_producto/', market_views.ProductoCreate.as_view(),name='crear_producto'),

    path('modificar_producto/',market_views.ProductosList.as_view(), name='modificar_producto'),

    path('modificar_producto/<int:pk>/',market_views.ProductoUpdate.as_view(), name='modificar_producto_x'),

    path('eliminar_producto/<int:pk>/',market_views.ProductoDelete.as_view(), name='eliminar_producto'),

    path('crear_categoria/', market_views.CategoriaCreate.as_view(),name='crear_categoria'),

    path('modificar_categoria/',market_views.CategoriasList.as_view(), name='modificar_categoria'),

    path('modificar_categoria/<int:pk>/',market_views.CategoriaUpdate.as_view(), name='modificar_categoria_x'),

    path('eliminar_categoria/<int:pk>/',market_views.CategoriaDelete.as_view(), name='eliminar_categoria'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
