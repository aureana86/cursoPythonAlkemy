from django.shortcuts import render, redirect
from django.db.models import Avg
from .models import Estudiante
from .forms import EstudianteForm


def bienvenida(request):
    return render(request, 'bienvenida.html')


def agregar_estudiante(request):
    if request.method == 'POST':
        form = EstudianteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mostrar_notas')
    else:
        form = EstudianteForm()
    return render(request, 'agregar_estudiante.html', {'form': form})


def mostrar_notas(request):
    estudiantes = Estudiante.objects.all()
    return render(request, 'estudiantes/mostrar_notas.html',
                  {'estudiantes': estudiantes})


def calcular_promedio(request):
    promedio = Estudiante.objects.aggregate(promedio=Avg('nota'))['promedio']
    return render(request, 'estudiantes/calcular_promedio.html',
                  {'promedio': promedio or 0})


def lista_estudiantes(request):
    estudiantes = Estudiante.objects.all()
    return render(request, 'estudiantes/lista_estudiantes.html',
                  {'estudiantes': estudiantes})


def detalle_estudiante(request, estudiante_id):
    estudiante = Estudiante.objects.get(id=estudiante_id)
    return render(request, 'estudiantes/detalle_estudiante.html',
                  {'estudiante': estudiante})


def editar_estudiante(request, estudiante_id):
    estudiante = Estudiante.objects.get(id=estudiante_id)
    if request.method == 'POST':
        form = EstudianteForm(request.POST, instance=estudiante)
        if form.is_valid():
            form.save()
            return redirect('lista_estudiantes')
    else:
        form = EstudianteForm(instance=estudiante)
    return render(request, 'estudiantes/editar_estudiante.html',
                  {'form': form})


def eliminar_estudiante(request, estudiante_id):
    estudiante = Estudiante.objects.get(id=estudiante_id)
    estudiante.delete()
    return redirect('lista_estudiantes')
