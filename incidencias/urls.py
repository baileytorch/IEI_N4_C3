from django.urls import path,include
from rest_framework import routers
from incidencias import views

enrutador = routers.DefaultRouter()

enrutador.register(r'paises', views.PaisViewSet)
enrutador.register(r'regiones', views.RegionViewSet)
enrutador.register(r'provincias',views.ProvinciaViewSet)

urlpatterns = [
    path('', include(enrutador.urls))
]