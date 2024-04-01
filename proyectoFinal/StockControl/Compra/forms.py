from django.forms import ModelForm
from .models import Proveedor, Producto


class ProveedorForm(ModelForm):
    class Meta:
        model = Proveedor
        fields = "__all__"


class ProductoForm(ModelForm):
    class Meta:
        model = Producto
        fields = "__all__"
