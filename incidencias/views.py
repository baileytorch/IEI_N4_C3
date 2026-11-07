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

class AutorListView(ListView):
    model = mod.Autor
    template_name = 'incidencias/autores/lista_autores.html'
    
class AutorCreateView(CreateView):
    form_class = fo.AutorForm
    model = mod.Autor
    success_url = 'listado_autores'
    template_name = 'incidencias/autores/crear_autor.html'

class AutorUpdateView(UpdateView):
    form_class = fo.AutorForm
    model = mod.Autor
    success_url = reverse_lazy('listado_autores')
    template_name = 'incidencias/autores/editar_autor.html'

class AutorDetailView(DetailView):
    form_class = fo.AutorForm
    model = mod.Autor
    template_name = 'incidencias/autores/detalle_autor.html'

class CambiarAutorHabilitadoView(UpdateView):
    form_class = fo.DeshabilitarAutorForm
    model = mod.Autor
    
    def form_valid(self, form):
        self.object = form.save()
        return redirect(self.request.META.get('HTTP_REFERER', '/'))

    def form_invalid(self, form):
        return redirect(self.request.META.get('HTTP_REFERER', '/'))