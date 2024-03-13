from django.db import models
from django.utils import timezone


class Tarea(models.Model):
    nombre = models.CharField(max_length=255)
    completada = models.BooleanField(default=False)
    responsable = models.CharField(max_length=255)
    fecha_inicio = models.DateField(default=timezone.now)
    fecha_termino = models.DateField(default=timezone.now)

    def __str__(self):
        return self.nombre


class Meta:
    app_label = 'nueva_app'
