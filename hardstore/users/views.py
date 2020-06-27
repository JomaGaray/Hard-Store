from django.shortcuts import render, redirect
from django.views.generic import View, ListView, TemplateView
from django.contrib.auth import authenticate, login, logout  # para la autenticacion
from django.views.generic.edit import CreateView

# permisos
from django.contrib.auth.mixins import UserPassesTestMixin
from .forms import CommonUserForm, ManagerUserForm, ExecutiveUserForm
from .models import CustomUser

# from django.contrib.auth.forms import UserCreationForm
# https://docs.djangoproject.com/en/3.0/topics/auth/ AUTENTICACION EN DJANGO


class CommonUserSignUpView(CreateView):
    model = CustomUser
    form_class = CommonUserForm
    template_name = 'users/signUp.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'commonUser'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/')


class ManagerUserSignUpView(UserPassesTestMixin, CreateView):
    model = CustomUser
    form_class = ManagerUserForm
    template_name = 'users/signUp.html'

    def test_func(self):
        return (self.request.user.is_managerUser) or (self.request.user.is_executiveUser)

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'managerUser'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/')


class ExecutiveUserSignUpView(UserPassesTestMixin, CreateView):
    model = CustomUser
    form_class = ExecutiveUserForm
    template_name = 'users/signUp.html'

    def test_func(self):
        return (self.request.user.is_managerUser) or (self.request.user.is_executiveUser)

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'executiveUser'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/')
