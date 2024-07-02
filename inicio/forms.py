from django import forms
from inicio.models import Guitar

class GuitarFormulario(forms.ModelForm):
    class Meta:
        model = Guitar
        fields = ['marca', 'forma']

class CrearGuitarFormulario(GuitarFormulario):
    class Meta:
        model = Guitar
        fields = ['marca', 'forma']

    def save(self, commit=True, user=None):
        guitar = super().save(commit=False)
        if user:
            guitar.user = user
        if commit:
            guitar.save()
        return guitar

class EditarGuitarFormulario(GuitarFormulario):
    class Meta:
        model = Guitar
        fields = ['marca', 'forma']

class BuscarGuitar(forms.Form):
    marca = forms.CharField(max_length=20, required=False)
