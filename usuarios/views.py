from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login as django_login, logout
from usuarios.forms import NuestroFormularioDeCreacion, EditarPerfil, VerPerfilForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from usuarios.models import DatosExtra

def login(request):
    formulario = AuthenticationForm()
    
    if request.method == 'POST':
        formulario = AuthenticationForm(data=request.POST)
        if formulario.is_valid():
            usuario = formulario.cleaned_data.get('username')
            contrasenia = formulario.cleaned_data.get('password')
        
            user = authenticate(request, username=usuario, password=contrasenia)

            if user is not None:
                django_login(request, user)
                DatosExtra.objects.get_or_create(user=user)
                return redirect('home')
    
    return render(request, 'usuarios/login.html', {'formulario': formulario})

def registro(request):
    formulario = NuestroFormularioDeCreacion()
    
    if request.method == "POST":
        formulario = NuestroFormularioDeCreacion(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('login')
    
    return render(request, 'usuarios/registro.html', {'formulario': formulario})

@login_required
def ver_perfil(request):
    datos_extra, created = DatosExtra.objects.get_or_create(user=request.user)
    form = VerPerfilForm(instance=datos_extra)
    return render(request, 'usuarios/ver_perfil.html', {'form': form})

@login_required
def editar_perfil(request):
    datos_extra, created = DatosExtra.objects.get_or_create(user=request.user)
    if request.method == "POST":
        formulario = EditarPerfil(request.POST, request.FILES, instance=request.user)
        if formulario.is_valid():
            formulario.save()
            avatar = formulario.cleaned_data.get('avatar')
            if avatar:
                datos_extra.avatar = avatar
            datos_extra.save()
            return redirect('ver_perfil')   
    else:
        formulario = EditarPerfil(instance=request.user)

    return render(request, 'usuarios/editar_perfil.html', {'formulario': formulario})

class CambiarPassword(PasswordChangeView):
    template_name = 'usuarios/cambiar_pass.html'
    success_url = reverse_lazy('editar_perfil')

def custom_logout(request):
    logout(request)
    return render(request, 'usuarios/logout_confirmation.html')
