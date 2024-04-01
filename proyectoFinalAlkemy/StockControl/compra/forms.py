from django.forms import ModelForm
from .models import Proveedor, Producto, Categoria


class ProveedorForm(ModelForm):
    class Meta:
        model = Proveedor
        fields = ['nombre', 'apellido', 'dni', 'cuil', 'celular',
                  'tipo_proveedor']


class ProductoForm(ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'precio', 'stock_actual', 'proveedor', 'categoria']


class CategoriaForm(ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre']
