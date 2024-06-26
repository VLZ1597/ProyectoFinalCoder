from django import forms

class GuitarFormulario(forms.Form):
    marca = forms.CharField(max_length=20)
    forma = forms.CharField(max_length=20)

class CrearGuitarFormulario(GuitarFormulario):
    ...

class EditarGuitarFormulario(GuitarFormulario):
    ...

class BuscarGuitar(forms.Form):
    marca= forms.CharField(max_length=20, required=False)