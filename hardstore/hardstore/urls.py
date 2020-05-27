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

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include('market.urls')), manera menos directa -Joma
    path('login/', user_views.VistaLogin.as_view(), name='login'),
    path('signup/', user_views.VistaSignup.as_view(), name='signup'),
  
    #path para productos de una categoria en particular
    path('productos/<str:categoria>/', market_views.ProductosList.as_view(), name='productosCategoria'),
  
  #path para un prodcuto en particular, un path dinamico <str:pk_prod>
    path('producto/<str:pk_producto>/', market_views.VistaUnProducto.as_view(), name='producto'),
    path('', market_views.VistaHome.as_view(), name='home'),
]
