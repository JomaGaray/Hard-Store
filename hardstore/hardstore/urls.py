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
from market.views import (
        index,SearchView,
        ProductoDetail,ProductosListCat,ProductosList,ProductoCreate,ProductoUpdate,ProductoDelete,ProductosCategoriaList,
        CategoriaCreate,CategoriaUpdate,CategoriaDelete,CategoriasList,
        ItemCreate,ItemDelete,
        LikeProduct,LikeProductList,LikeDelete,
        CarritoList,CompraView
    )
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index.as_view(), name='home'),
    path('', include('users.urls')),


    # Busqueda de productos
    path('search/', SearchView.as_view(), name='search'),
    
    path('producto/<int:pk_producto>/',ProductoDetail.as_view(), name='producto-detalle'),
    path('productos_categoria/<int:pk_categoria>',ProductosCategoriaList.as_view(), name='productos-categoria-list'),

    

    path('carrito/', CarritoList.as_view(), name='carrito'),

    path('add-carrito/<int:pk_producto>/', ItemCreate.as_view(), name='carrito-add'),

    path('eliminar-item/<int:pk>/',ItemDelete.as_view(), name='eliminar-item'),


    path('compra_concretada/', CompraView.as_view(), name='compra_concretada'),

    # ------PRUEBA DE LIKES

    path('likeProducto/<int:pk_producto>',LikeProduct.as_view(), name='Like'),

    path('LikeList/',LikeProductList.as_view(), name='LikeList'),

    path('eliminar-like/<int:pk>/',LikeDelete.as_view(), name='eliminar-like'),
    
    # -------Administracion-------
    path('crear_producto/', ProductoCreate.as_view(),name='crear_producto'),

    path('modificar_producto/', ProductosList.as_view(),name='modificar_producto'),

    path('modificar_producto/<int:pk_categoria>', ProductosListCat.as_view(),name='modificar_producto_cat'),

    path('modificar_producto/<int:pk>/',ProductoUpdate.as_view(), name='modificar_producto_x'),

    path('eliminar_producto/<int:pk>/',ProductoDelete.as_view(), name='eliminar_producto'),

    path('crear_categoria/', CategoriaCreate.as_view(),name='crear_categoria'),

    path('modificar_categoria/', CategoriasList.as_view(),name='modificar_categoria'),

    path('modificar_categoria/<int:pk>/',CategoriaUpdate.as_view(), name='modificar_categoria_x'),

    path('eliminar_categoria/<int:pk>/',CategoriaDelete.as_view(), name='eliminar_categoria'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
