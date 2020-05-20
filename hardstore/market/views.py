from django.shortcuts import render
from django.http import HttpResponse,HttpRequest
from .models import Category,Product,Order,Customer
from django.views import View
import datetime

class VistaHome(View):
	def get(self,request):
		products = Product.objects.all()
		context = {'titulo':'Home','products' : products }
		return render(request, 'home.html', context)
	
