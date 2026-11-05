from django.shortcuts import render
from django.views.generic import ListView,CreateView
from rest_framework import viewsets

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