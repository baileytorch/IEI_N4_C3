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
                    'type':'text',
                    'class': 'form-control',
                    'placeholder':'Nombre Autor...'
                }
            ),
            'pseudonimo': forms.TextInput(
                attrs = {
                    'type':'text',
                    'class': 'form-control',
                    'placeholder':'Pseudónimo Autor...'
                }
            ),
            'nacionalidad': forms.Select(
                attrs = {
                    'class': 'form-select'
                }
            ),
            'fecha_nacimiento': forms.DateInput(
                format="%Y-%m-%d",
                attrs = {
                    'type':'date',               
                    'class': 'form-control'
                }
            ),
            'fecha_defuncion': forms.DateInput(
                format="%Y-%m-%d",
                attrs = {
                    'type':'date',               
                    'class': 'form-control'
                }
            ),
            'biografia': forms.Textarea(
                attrs = {
                    'type':'text',
                    'class': 'form-control',
                    'placeholder':'Biografía Autor...',
                    'rows': 5
                }
            )
        }
        
class DeshabilitarAutorForm(forms.ModelForm):
    class Meta:
        model = mo.Autor
        fields = ['habilitado']