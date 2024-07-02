from django.shortcuts import render, redirect
from inicio.models import Guitar
from inicio.forms import CrearGuitarFormulario, BuscarGuitar
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Count
from django.http import HttpResponseForbidden
from django.views.generic.edit import DeleteView, UpdateView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

def inicio(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

@login_required
def crear_guitar(request):
    formulario = CrearGuitarFormulario()

    if request.method == 'POST':
        formulario = CrearGuitarFormulario(request.POST)
        if formulario.is_valid():
            datos = formulario.cleaned_data
            marca = datos.get('marca')
            forma = datos.get('forma')
            
            marcas_validas = ['Gibson', 'Fender', 'PRS']
            formas_validas = ['LesPaul', 'Stratocaster', 'Custom 24']
            
            if marca not in marcas_validas or forma not in formas_validas:
                messages.error(request, 'Por favor ingresa una marca y forma válidas.')
            else:
                guitar = Guitar(marca=marca, forma=forma, user=request.user)
                guitar.save()
                messages.success(request, 'Guitar creada exitosamente.')
                return redirect('guitars')
        else:
            messages.error(request, 'Por favor corrige los errores en el formulario.')

    return render(request, 'inicio/crear_guitar.html', {'formulario': formulario})

def guitars(request):
    formulario = BuscarGuitar(request.GET)
    if formulario.is_valid():
        marca = formulario.cleaned_data['marca']
        guitars = Guitar.objects.filter(marca__icontains=marca)
    else:
        guitars = Guitar.objects.all()

    guitar_by_brand = Guitar.objects.values('marca').annotate(total=Count('marca')).order_by('-total')
    top_brand = guitar_by_brand.first() if guitar_by_brand else None

    return render(request, 'inicio/guitars.html', {
        'guitars': guitars,
        'formulario': formulario,
        'guitar_by_brand': guitar_by_brand,
        'top_brand': top_brand
    })

class EliminarGuitar(LoginRequiredMixin, DeleteView):
    model = Guitar
    template_name = 'inicio/eliminar_guitar.html'
    success_url = reverse_lazy('guitars')

    def get_object(self, queryset=None):
        guitar = super().get_object(queryset)
        if guitar.user != self.request.user:
            return HttpResponseForbidden("No tienes permiso para eliminar esta guitarra.")
        return guitar

class EditarGuitar(LoginRequiredMixin, UpdateView):
    model = Guitar
    template_name = 'inicio/editar_guitar.html'
    success_url = reverse_lazy('guitars')
    fields = ['marca', 'forma']

    def get_object(self, queryset=None):
        guitar = super().get_object(queryset)
        if guitar.user != self.request.user:
            return HttpResponseForbidden("No tienes permiso para editar esta guitarra.")
        return guitar

class VerGuitar(DetailView):
    model = Guitar
    template_name = 'inicio/ver_guitar.html'
