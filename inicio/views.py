from django.shortcuts import render , redirect
from inicio.models import Guitar
from inicio.forms import CrearGuitarFormulario , EditarGuitarFormulario , BuscarGuitar
from django.contrib.auth.decorators import login_required


def inicio(request):
    return render(request, 'inicio/index.html')

def about(request): 
    return render(request, 'about.html')

def crear_guitar(request):

    formulario = CrearGuitarFormulario() 
    
    if request.method == 'POST':
        formulario = CrearGuitarFormulario(request.POST)
        if formulario.is_valid():
            datos = formulario.cleaned_data
            guitar=Guitar(marca=datos.get('marca'), forma=datos.get('forma'))
            guitar.save()
            return redirect('guitars')
            
    return render(request, 'inicio/crear_guitar.html', {'formulario': formulario})

def guitars(request):
    
    formulario = BuscarGuitar(request.GET)
    if formulario.is_valid():   
        marca = formulario.cleaned_data['marca']        
        guitar = Guitar.objects.filter(marca__icontains=marca)

    return render(request,'guitars.html', {'guitars': guitar ,'formulario': formulario})

def eliminar_guitar(request,id):
    guitar = Guitar.objects.get(id=id)
    guitar.delete()
    return redirect('guitars')

    
def editar_guitar(request, id):
    guitar = Guitar.objects.get(id=id)
    
    formulario = EditarGuitarFormulario(initial={'marca': guitar.marca, 'modelo': guitar.forma})
    
    if request.method == 'POST':
        formulario = EditarGuitarFormulario(request.POST)
        if formulario.is_valid():
            info = formulario.cleaned_data
            
            guitar.marca = info['marca']
            guitar.forma = info['forma']
            guitar.save()
            return redirect('guitars')
    
    return render(request, 'inicio/editar_guitar.html', {'formulario': formulario, 'guitar': guitar})


def ver_guitar(request,id):
    guitar = Guitar.objects.get(id=id)
    return render(request, 'inicio/ver_guitar.html', {'guitar': guitar})