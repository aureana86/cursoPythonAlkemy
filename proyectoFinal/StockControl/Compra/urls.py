from django.urls import path
from .views import agregar_proveedor, agregar_producto, inicio
from .views import listar_opciones, producto_list, proveedor_list

urlpatterns = [
    path('', inicio, name='inicio'),
    path('agregar_proveedor/', agregar_proveedor, name='agregar_proveedor'),
    path('agregar_producto/', agregar_producto, name='agregar_producto'),
    path('listar_opciones/', listar_opciones, name='listar_opciones'),
    path('producto_list/', producto_list, name='producto_list'),
    path('proveedor_list/', proveedor_list, name='proveedor_list'),
]
