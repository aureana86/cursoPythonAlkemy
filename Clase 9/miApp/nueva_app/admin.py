from django.contrib import admin
from . models import Tarea


class TareaAdmin(admin.ModelAdmin):
    list_display = ["nombre", "completada", "responsable", "fecha_inicio", "fecha_termino"]
    search_fields = ["nombre", "completada", "responsable", "fecha_inicio", "fecha_termino"]


admin.site.register(Tarea, TareaAdmin)
