from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from .models import CustomUser

# se renderizan los dos forms juntos en el templates


class CommonUserForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'first_name', 'last_name',
                  'email', 'password1', 'password2',)

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_commonUser = True
        if commit:
            user.save()
        return user


class ManagerUserForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'first_name', 'last_name',
                  'email', 'password1', 'password2',)

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_managerUser = True
        if commit:
            user.save()
        return user


class ExecutiveUserForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'first_name', 'last_name',
                  'email', 'password1', 'password2',)

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_executiveUser = True
        if commit:
            user.save()
        return user


"""
class UserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name',
                  'email', 'password1', 'password2',)


class AdminForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('is_staff', 'username', 'first_name', 'last_name',
                  'email', 'password1', 'password2', )
"""
