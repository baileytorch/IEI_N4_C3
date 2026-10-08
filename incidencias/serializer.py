from rest_framework import serializers
from .models import Pais, Region, Provincia, Comuna
from .models import Direccion
from .models import Biblioteca
from .models import Autor
from .models import Genero
from .models import SubGenero
from .models import Editorial
from .models import Idioma
from .models import Edicion
from .models import Libro
from .models import Estado
from .models import Ubicacion
from .models import Inventario
from .models import Usuario
from .models import Prestamo

class PaisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pais
        fields = ('nombre','nacionalidad','iso_2','iso_3')

class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ('codigo','region')

class ProvinciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provincia
        fields = ('codigo','provincia','region')