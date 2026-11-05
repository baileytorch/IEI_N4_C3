from django import forms
from . import models as mo

class AutorForm(forms.ModelForm):
    class Meta:
        model = mo.Autor
        fields = [
            'nombre',
            'pseudonimo',
            'nacionalidad',
            'fecha_nacimiento',
            'fecha_defuncion',
            'biografia'
        ]