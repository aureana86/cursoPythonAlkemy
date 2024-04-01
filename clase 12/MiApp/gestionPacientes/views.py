from django.template import loader
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect
from .models import Paciente
from .forms import PacienteForm


def lista_pacientes(request):
    template = loader.get_template('tu_app/lista_pacientes.html')
    pacientes = Paciente.objects.all()
    context = {
        'pacientes': pacientes,
    }
    return HttpResponse(template.render(context, request))


def detalles_paciente(request, paciente_id):
    template = loader.get_template('tu_app/detalles_paciente.html')
    paciente = get_object_or_404(Paciente, pk=paciente_id)
    context = {
        'paciente': paciente,
    }
    return HttpResponse(template.render(context, request))


def crear_paciente(request):
    template = loader.get_template('tu_app/crear_paciente.html')
    if request.method == 'POST':
        form = PacienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_pacientes')
    else:
        form = PacienteForm()
    context = {
        'form': form,
    }
    return HttpResponse(template.render(context, request))


def editar_paciente(request, paciente_id):
    template = loader.get_template('tu_app/editar_paciente.html')
    paciente = get_object_or_404(Paciente, pk=paciente_id)
    if request.method == 'POST':
        form = PacienteForm(request.POST, instance=paciente)
        if form.is_valid():
            form.save()
            return redirect('lista_pacientes')
    else:
        form = PacienteForm(instance=paciente)
    context = {
        'form': form,
    }
    return HttpResponse(template.render(context, request))


def eliminar_paciente(request, paciente_id):
    template = loader.get_template('tu_app/eliminar_paciente.html')
    paciente = get_object_or_404(Paciente, pk=paciente_id)
    if request.method == 'POST':
        paciente.delete()
        return redirect('lista_pacientes')
    context = {
        'paciente': paciente,
    }
    return HttpResponse(template.render(context, request))
