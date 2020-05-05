from django.shortcuts import render

def home(request):

	return render(request,'home.html',{'titulo':'Home'})

def login(request):

	return render(request,'LogIn.html')
# Create your views here.
