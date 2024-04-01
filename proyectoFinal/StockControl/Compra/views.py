from django.shortcuts import render, redirect
from .models import Producto, Proveedor
from .forms import ProveedorForm, ProductoForm


def inicio(request):
    return render(request, 'inicio.html')


def listar_opciones(request):
    if request.method == 'POST':
        opcion = request.POST.get('opcion')
        if opcion == 'productos':
            return redirect('producto_list')
        elif opcion == 'proveedores':
            return redirect('proveedor_list')
    return render(request, 'listar_opciones.html')


def producto_list(request):
    productos = Producto.objects.all()
    template = 'producto_list.html'
    return render(request, template, {'productos': productos})


def proveedor_list(request):
    proveedores = Proveedor.objects.all()
    template = 'proveedor_list.html'
    return render(request, template, {'proveedores': proveedores})


def agregar_proveedor(request):
    if request.method == 'POST':
        form = ProveedorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('agregar_proveedor')
    else:
        form = ProveedorForm()
    return render(request, 'compra/agregar_proveedor.html', {'form': form})


def agregar_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('agregar_producto')
    else:
        form = ProductoForm()
    return render(request, 'compra/agregar_producto.html', {'form': form})
