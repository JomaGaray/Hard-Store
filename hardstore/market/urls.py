from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name='hardstore-home'),
    path('/login', views.login, name='hardstore-login'),
]