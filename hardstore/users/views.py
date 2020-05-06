from django.shortcuts import render


def login(request):

    return render(request, 'login.html', {'titulo': 'Login'})


def regitro(request):

    return render(request, 'registro.html', {'titulo': 'Registro'})

