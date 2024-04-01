from django.shortcuts import render, redirect
from .models import Estudiante

def agregar_estudiante(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        apellido = request.POST['apellido']
        edad = request.POST['edad']
        nota = request.POST['nota']
        Estudiante.objects.create(nombre=nombre, apellido=apellido, edad=edad, nota=nota)
        return redirect('mostrar_notas')
    return render(request, 'agregar_estudiante.html')

def mostrar_notas(request):
    estudiantes = Estudiante.objects.all()
    return render(request, 'mostrar_notas.html', {'estudiantes': estudiantes})

def calcular_promedio(request):
    estudiantes = Estudiante.objects.all()
    total_notas = 0
    cantidad_estudiantes = 0
    for estudiante in estudiantes:
        total_notas += estudiante.nota
        cantidad_estudiantes += 1
    promedio = total_notas / cantidad_estudiantes if cantidad_estudiantes != 0 else 0
    return render(request, 'calcular_promedio.html', {'promedio': promedio})