from django.urls import path
from .views import categorias, inicio, agregar_proveedor, agregar_producto
from .views import producto_list, proveedor_list
from .views import editar_producto, editar_proveedor
from .views import borrar_producto, borrar_proveedor
from .views import agregar_categoria, editar_categoria, eliminar_categoria


urlpatterns = [
    path('', inicio, name='inicio'),
    path('producto_list/', producto_list, name='producto_list'),
    path('proveedor_list/', proveedor_list, name='proveedor_list'),
    path('agregar_proveedor/', agregar_proveedor, name='agregar_proveedor'),
    path('agregar_producto/', agregar_producto, name='agregar_producto'),
    path('editar_producto/<int:producto_id>/', editar_producto,
         name='editar_producto'),
    path('borrar_producto/<int:producto_id>/', borrar_producto,
         name='borrar_producto'),
    path('editar_proveedor/<int:proveedor_id>/', editar_proveedor,
         name='editar_proveedor'),
    path('borrar_proveedor/<int:proveedor_id>/', borrar_proveedor,
         name='borrar_proveedor'),
    path('categorias/', categorias, name='categorias'),
    path('agregar_categoria/', agregar_categoria, name='agregar_categoria'),
    path('editar_categoria/<int:id>/', editar_categoria,
         name='editar_categoria'),
    path('eliminar_categoria/<int:id>/', eliminar_categoria,
         name='eliminar_categoria'),
]
