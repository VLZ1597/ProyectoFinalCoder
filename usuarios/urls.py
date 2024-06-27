from django.urls import path 
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/',views.login, name='login'),
    path('logout/', LogoutView.as_view(template_name='Usuarios/logout.html'), name='logout'),
    path('registro/', views.registro, name='register'),
    path('perfil/editar/', views.editar_perfil, name='editar_perfil'),
    path('perfil/editar/password/', views.CambiarPassword.as_view(), name='cambiar_pass'),
]
