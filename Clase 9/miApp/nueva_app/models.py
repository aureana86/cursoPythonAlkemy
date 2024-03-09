from django.db import models


class Tarea(models.Model):
    nombre = models.CharField(max_length=255)
    completada = models.BooleanField(default=False)
    responsable = models.CharField(max_length=255)
    fecha_inicio = models.DateField()
    fecha_termino = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.nombre


class Meta:
    app_label = 'nueva_app'
