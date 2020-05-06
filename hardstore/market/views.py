from django.shortcuts import render


def home(request):

    return render(request, 'home.html', {'titulo': 'Home'})

# Create your views here.


def login(request):
    return render(request, 'LogIn.html')
