from django.shortcuts import render
from django.views.generic import View,ListView,TemplateView


class VistaSignup(View):
	def get(self,request):
		return render(request,  'signup.html', {'titulo': 'SignUp'})

class VistaLogin(View):
	def get(self,request):
		return render(request, 'login.html', {'titulo': 'Login'})

# Corey - 
#   https://www.youtube.com/watch?v=q4jPR-M0TAQ&list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p&index=6
#   https://www.youtube.com/watch?v=3aVqWaLjqS4&list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p&index=7
#
# Hay que fijarse en los templates los formularios ( form )
#
#
#from django.contrib.auth.forms import UserCreationForm
#
#class VistaSignup(View):
#	def get(self,request):
#		form = UserCreationForm()		
#		return render(request,  'signup.html', {'titulo': 'SignUp','form':form})
#
#	def post(self,request):
#		form = UserCreationForm(request.POST)
#		if form.is_valid():
#			form.save()
#			username = form.cleaned_data.get('username')
#			return redirect('login')
#		return render(request,  'signup.html', {'titulo': 'SignUp','form':form})
