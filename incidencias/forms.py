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
        widgets = {
            'nombre': forms.TextInput(
                attrs = {
                    'class': 'form-control'
                }
            ),
            'pseudonimo': forms.TextInput(
                attrs = {
                    'class': 'form-control'
                }
            ),
            'nacionalidad': forms.Select(
                attrs = {
                    'class': 'form-select'
                }
            )
        }