from django.urls import path
from . import views
from .views import lista_estudiantes, detalle_estudiante, agregar_estudiante
from .views import editar_estudiante, eliminar_estudiante

urlpatterns = [
    path('lista/', lista_estudiantes, name='lista_estudiantes'),
    path('detalle/<int:estudiante_id>/',
         detalle_estudiante, name='detalle_estudiante'),
    path('agregar/', agregar_estudiante, name='agregar_estudiante'),
    path('agregar_estudiante/', views.agregar_estudiante,
         name='agregar_estudiante'),
    path('editar/<int:estudiante_id>/',
         editar_estudiante, name='editar_estudiante'),
    path('eliminar/<int:estudiante_id>/',
         eliminar_estudiante, name='eliminar_estudiante'),
]
