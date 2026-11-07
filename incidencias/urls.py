from django.urls import path,include
from rest_framework import routers
from incidencias import views

enrutador = routers.DefaultRouter()

enrutador.register(r'paises', views.PaisViewSet)
enrutador.register(r'regiones', views.RegionViewSet)
enrutador.register(r'provincias',views.ProvinciaViewSet)

urlpatterns = [
    path('', include(enrutador.urls)),
    path('autores/listado_autores', views.AutorListView.as_view(), name='listado_autores'),
    path('autores/crear_autor', views.AutorCreateView.as_view(), name='crear_autor'),
    path('autores/<int:pk>/editar_autor', views.AutorUpdateView.as_view(), name='editar_autor'),
    path('autores/<int:pk>/detalle_autor', views.AutorDetailView.as_view(), name='detalle_autor'),
    path('autores/<int:pk>/deshabilitar_autor', views.CambiarAutorHabilitadoView.as_view(), name='deshabilitar_autor')
]