from django.urls import path
from .views import tarea_list, tarea_detail
from .views import tarea_create, tarea_update, tarea_delete, inicio

urlpatterns = [
    path('', inicio, name='inicio'),
    path('tareas/', tarea_list, name='tarea-list'),
    path('tareas/<int:pk>/', tarea_detail, name='tarea-detail'),
    path('tareas/nueva/', tarea_create, name='tarea-create'),
    path('tareas/<int:pk>/editar/', tarea_update, name='tarea-update'),
    path('tareas/<int:pk>/eliminar/', tarea_delete, name='tarea-delete'),
]
