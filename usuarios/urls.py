from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.custom_logout, name='logout'),
    path('registro/', views.registro, name='register'),
    path('perfil/ver/', views.ver_perfil, name='ver_perfil'),
    path('perfil/editar/', views.editar_perfil, name='editar_perfil'),
    path('perfil/editar/password/', views.CambiarPassword.as_view(), name='cambiar_pass'),
]
