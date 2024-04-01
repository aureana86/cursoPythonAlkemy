from django.db import models


class Paciente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    genero = models.CharField(max_length=10)
    direccion = models.TextField()

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
