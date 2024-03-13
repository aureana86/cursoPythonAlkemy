from django.db import models


class Estudiante(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    edad = models.IntegerField()
    nota = models.DecimalField(max_digits=5, decimal_places=2)
