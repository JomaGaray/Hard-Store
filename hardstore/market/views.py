from django.shortcuts import render
from django.http import HttpResponse,HttpRequest
from django.views import View
import datetime

def home(request):

    return render(request, 'home.html', {'titulo': 'Home'})

class VistaHora(View):
	def get(self,request: HttpRequest):
		now = datetime.datetime.now()
		return HttpResponse(F"<html><body>la hora es:{now}  </body></html>") 
