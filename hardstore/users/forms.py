from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Cliente
from django.contrib.auth.models import User


class CreateUserForm(UserCreationForm):

    class Meta:
        model = User  # un User que provee Django
        fields = ['username', 'email', 'password1',
                  'password2', 'first_name', 'last_name', 'is_superuser']
