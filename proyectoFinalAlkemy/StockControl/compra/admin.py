from django.contrib import admin
from .models import Producto, Proveedor, Categoria


class ProductoAdmin(admin.ModelAdmin):
    list_display = ["nombre", "precio", "stock_actual",
                    "proveedor", "categoria"]
    search_fields = ["nombre", "precio", "stock_actual",
                     "proveedor__nombre", "categoria__nombre"]


class ProveedorAdmin(admin.ModelAdmin):
    list_display = ["nombre", "apellido", "dni", "tipo_proveedor", "cuil"]
    search_fields = ["nombre", "apellido", "dni", "cuil"]


class CategoriaAdmin(admin.ModelAdmin):
    list_display = ["nombre"]
    search_fields = ["nombre"]


admin.site.register(Producto, ProductoAdmin)
admin.site.register(Proveedor, ProveedorAdmin)
admin.site.register(Categoria, CategoriaAdmin)
