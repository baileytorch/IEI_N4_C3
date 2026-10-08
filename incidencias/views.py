from django.shortcuts import render
from rest_framework import viewsets

from .models import Pais, Region, Provincia, Comuna, Direccion, Biblioteca, Autor, Genero, SubGenero
from .models import Editorial, Idioma, Edicion, Libro, Estado, Ubicacion, Inventario, Usuario, Prestamo

from .serializer import PaisSerializer,RegionSerializer,ProvinciaSerializer

def bienvenida(request):
    return render(request, 'bienvenida.html')

class PaisViewSet(viewsets.ModelViewSet):
    queryset = Pais.objects.all()
    serializer_class = PaisSerializer

class RegionViewSet(viewsets.ModelViewSet):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer

class ProvinciaViewSet(viewsets.ModelViewSet):
    queryset = Provincia.objects.all()
    serializer_class = ProvinciaSerializer