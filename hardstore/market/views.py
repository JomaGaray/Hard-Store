from django.shortcuts import render
from django.http import HttpResponse,HttpRequest
from .models import Category,Product,Order,Customer
import datetime

def home(request):
	products = Product.objects.all()
	return render(request, 'home.html', {'titulo':'Home','products' : products })
	
