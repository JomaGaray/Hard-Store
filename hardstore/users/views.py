from django.shortcuts import render


def login(request):

    return render(request, 'login.html', {'titulo': 'Login'})


def signup(request):

    return render(request, 'signup.html', {'titulo': 'SignUp'})
