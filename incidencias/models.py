from django.db import models

# Create your models here.
class Pais(models.Model):
    nombre = models.CharField(max_length=60,null=False)
    nacionalidad = models.CharField(max_length=20,null=False)
    iso_2 = models.CharField(max_length=2,null=False)
    iso_3 = models.CharField(max_length=3,null=False)
    habilitado = models.BooleanField(default=True)

class Autor(models.Model):
    nombre = models.CharField(max_length=100,null=True)
    pseudonimo = models.CharField(max_length=50,null=True)
    nacionalidad = models.ForeignKey(Pais, on_delete=models.CASCADE)
    fecha_nacimiento = models.DateField(null=True)
    fecha_defuncion = models.DateField(null=True)
    habilitado = models.BooleanField(default=True)