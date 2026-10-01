from rest_framework import serializers
from .models import Pais
from .models import Region
from .models import Provincia
from .models import Comuna
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
        # fields = '__all__' # Esta definición trae todos los campos del modelo al serializador
        fields = ('nombre','nacionalidad','iso_2','iso_3')