from django import forms
from inicio.models import Guitar

class GuitarFormulario(forms.ModelForm):
    class Meta:
        model = Guitar
        fields = ['marca', 'forma', 'comentario']

class CrearGuitarFormulario(GuitarFormulario):
    class Meta:
        model = Guitar
        fields = ['marca', 'forma', 'comentario']

    def save(self, commit=True, user=None):
        guitar = super().save(commit=False)
        if user:
            guitar.user = user
        guitar.load_count += 1
        if commit:
            guitar.save()
        return guitar

class EditarGuitarFormulario(GuitarFormulario):
    class Meta:
        model = Guitar
        fields = ['marca', 'forma', 'comentario']

class BuscarGuitar(forms.Form):
    marca = forms.CharField(max_length=20, required=False)
