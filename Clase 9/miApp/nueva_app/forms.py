from django import forms
from .models import Tarea


class TareaForm(forms.ModelForm):
    class Meta:
        model = Tarea
        fields = ['nombre', 'completada',
                  'responsable', 'fecha_inicio', 'fecha_termino']
