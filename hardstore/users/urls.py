from django.contrib import admin
from django.urls import path, include
# traigo las vistas de usuarios, mas directo -Joma
from users import views as user_views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [

	# autenticacion
    path('accounts/', include('django.contrib.auth.urls')),
    # para el 'login_url' de las vistas, necesito hacer un url especifico, esto esta en la docu
    path('accounts/login/', include('django.contrib.auth.urls'), name='login'),

    # signUp de distintos Usuarios
    path('signup/CommonUser/',user_views.CommonUserSignUpView.as_view(), name='signup'),

    path('signup/ManagerUser/',user_views.ManagerUserSignUpView.as_view(), name='signupManagerUser'),

    path('signup/ExecutiveUser/',user_views.ExecutiveUserSignUpView.as_view(), name='signupExecutiveUser'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
