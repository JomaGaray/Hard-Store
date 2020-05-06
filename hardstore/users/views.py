from django.shortcuts import render


def login(request):

    return render(request, 'login.html', {'titulo': 'Login'})

# Create your views here.
