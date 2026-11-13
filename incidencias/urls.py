from django.urls import path,include
from rest_framework import routers
from incidencias import views

enrutador = routers.DefaultRouter()

enrutador.register(r'paises', views.PaisViewSet)
enrutador.register(r'regiones', views.RegionViewSet)
enrutador.register(r'provincias',views.ProvinciaViewSet)

urlpatterns = [
    path('', include(enrutador.urls)),
    path('autores/listado_autores', views.ListadoAutores.as_view(), name='listado_autores'),
    path('autores/crear_autor', views.CrearAutor.as_view(), name='crear_autor'),
    path('autores/<int:pk>/editar_autor', views.ActualizarAutor.as_view(), name='editar_autor'),
    path('autores/<int:pk>/detalle_autor', views.DetalleAutor.as_view(), name='detalle_autor'),
    path('autores/<int:pk>/deshabilitar_autor', views.CambiarEstadoAutor.as_view(), name='deshabilitar_autor'),
    path('libros/listado_libros', views.ListadoLibros.as_view(), name='listado_libros'),
    path('libros/crear_libro', views.CrearLibro.as_view(), name='crear_libro'),
    path('libros/<int:pk>/editar_libro', views.ActualizarLibro.as_view(), name='editar_libro'),
    path('libros/<int:pk>/detalle_libro', views.DetalleLibro.as_view(), name='detalle_libro'),
    path('libros/<int:pk>/deshabilitar_libro', views.CambiarEstadoLibro.as_view(), name='deshabilitar_libro')
]