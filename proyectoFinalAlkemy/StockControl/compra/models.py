from django.db import models


class Proveedor(models.Model):
    MAYORISTA = 'M'
    MINORISTA = 'm'
    TIPO_PROVEEDOR_CHOICES = [
        (MAYORISTA, 'Mayorista'),
        (MINORISTA, 'Minorista'),
    ]
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100, blank=True, null=True)
    dni = models.IntegerField(blank=True, null=True)
    cuil = models.CharField(max_length=20, blank=True, null=True)
    celular = models.CharField(max_length=20, blank=True, null=True)
    tipo_proveedor = models.CharField(max_length=1,
                                      choices=TIPO_PROVEEDOR_CHOICES)

    def __str__(self):
        return (
                f"{self.nombre} {self.apellido}"
                if self.tipo_proveedor == Proveedor.MINORISTA
                else self.nombre
               )


class Producto(models.Model):
    nombre = models.CharField(max_length=255)
    precio = models.FloatField()
    stock_actual = models.IntegerField()
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    categoria = models.ForeignKey('Categoria',
                                  on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.nombre


class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


def agregar_categorias():
    categorias_nuevas = ['Indumentaria', 'Equipamiento', 'Otros']
    for nombre_categoria in categorias_nuevas:
        Categoria.objects.get_or_create(nombre=nombre_categoria)
