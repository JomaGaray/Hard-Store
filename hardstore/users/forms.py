from django.forms import ModelForm
from .models import Profile
from django.contrib.auth.models import User

#se renderizan los dos forms juntos en el templates

#class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1',
                  'password2', 'first_name', 'last_name', 'is_superuser']

#class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ('birth_date')

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=100, help_text='Last Name')
    last_name = forms.CharField(max_length=100, help_text='Last Name')
    email = forms.EmailField(max_length=150, help_text='Email')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name',
                'email', 'password1', 'password2',)