from django.shortcuts import render,redirect
from django.contrib import messages
from django.views.generic import ListView,CreateView,UpdateView,DetailView
from django.urls import reverse_lazy
from rest_framework import viewsets
from django.http import JsonResponse

from . import models as mod
from . import serializer as ser
from . import forms as fo

def bienvenida(request):
    return render(request, 'bienvenida.html')

class PaisViewSet(viewsets.ModelViewSet):
    queryset = mod.Pais.objects.all()
    serializer_class = ser.PaisSerializer

class RegionViewSet(viewsets.ModelViewSet):
    queryset = mod.Region.objects.all()
    serializer_class = ser.RegionSerializer

class ProvinciaViewSet(viewsets.ModelViewSet):
    queryset = mod.Provincia.objects.all()
    serializer_class = ser.ProvinciaSerializer

class ListadoAutores(ListView):
    model = mod.Autor
    template_name = 'incidencias/autores/lista_autores.html'
    
class CrearAutor(CreateView):
    form_class = fo.FormularioAutor
    model = mod.Autor
    success_url = 'listado_autores'
    template_name = 'incidencias/autores/crear_autor.html'

class ActualizarAutor(UpdateView):
    form_class = fo.FormularioAutor
    model = mod.Autor
    success_url = reverse_lazy('listado_autores')
    template_name = 'incidencias/autores/editar_autor.html'

class DetalleAutor(DetailView):
    form_class = fo.FormularioAutor
    model = mod.Autor
    template_name = 'incidencias/autores/detalle_autor.html'

class CambiarEstadoAutor(UpdateView):
    form_class = fo.FormularioCambiarEstadoAutor
    model = mod.Autor
    
    def form_valid(self, form):
        self.object = form.save()
        return redirect(self.request.META.get('HTTP_REFERER', '/'))

    def form_invalid(self, form):
        return redirect(self.request.META.get('HTTP_REFERER', '/'))

class ListadoLibros(ListView):
    model = mod.Libro
    template_name = 'incidencias/libros/lista_libros.html'
    
class CrearLibro(CreateView):
    form_class = fo.FormularioLibro
    model = mod.Libro
    success_url = 'listado_libros'
    template_name = 'incidencias/libros/formulario_libro.html'

class ActualizarLibro(UpdateView):
    form_class = fo.FormularioLibro
    model = mod.Libro
    success_url = reverse_lazy('listado_libros')
    template_name = 'incidencias/libros/formulario_libro.html'

class DetalleLibro(DetailView):
    form_class = fo.FormularioLibro
    model = mod.Autor
    template_name = 'incidencias/libros/detalle_libro.html'

class CambiarEstadoLibro(UpdateView):
    form_class = fo.FormularioCambiarEstadoLibro
    model = mod.Libro
    
    def form_valid(self, form):
        self.object = form.save()
        return redirect(self.request.META.get('HTTP_REFERER', '/'))

    def form_invalid(self, form):
        return redirect(self.request.META.get('HTTP_REFERER', '/'))