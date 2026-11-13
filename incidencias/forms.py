from django import forms
from . import models as mo

str_opcion = '-- Selecciona una opción --'

class FormularioAutor(forms.ModelForm):
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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nacionalidad'].empty_label = str_opcion
        
class FormularioCambiarEstadoAutor(forms.ModelForm):
    class Meta:
        model = mo.Autor
        fields = ['habilitado']

class FormularioLibro(forms.ModelForm):
    class Meta:
        model = mo.Libro
        fields = [
            'titulo',
            'paginas',
            'autor',
            'subgenero',
            'edicion',
            'biblioteca'
        ]
        widgets = {
            'titulo': forms.TextInput(
                attrs = {
                    'type':'text',
                    'class': 'form-control',
                    'placeholder':'Título Libro...'
                }
            ),
            'paginas': forms.NumberInput(
                attrs = {
                    'type':'number',
                    'class': 'form-control'
                }
            ),
            'autor': forms.Select(
                attrs = {
                    'class': 'form-select'
                }
            ),
            'subgenero': forms.Select(
                attrs = {
                    'class': 'form-select'
                }
            ),
            'edicion': forms.Select(
                attrs = {
                    'class': 'form-select'
                }
            ),
            'biblioteca': forms.Select(
                attrs = {
                    'class': 'form-select'
                }
            )
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['autor'].empty_label = str_opcion
        self.fields['subgenero'].empty_label = str_opcion
        self.fields['edicion'].empty_label = str_opcion
        self.fields['biblioteca'].empty_label = str_opcion
        
class FormularioCambiarEstadoLibro(forms.ModelForm):
    class Meta:
        model = mo.Autor
        fields = ['habilitado']