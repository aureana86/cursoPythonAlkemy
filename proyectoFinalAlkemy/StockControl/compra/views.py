from django.shortcuts import get_object_or_404, render, redirect
from .models import Producto, Proveedor, Categoria
from .forms import ProveedorForm, ProductoForm


def inicio(request):
    return render(request, 'inicio.html')


def categorias(request):
    categorias = Categoria.objects.all()
    return render(request, 'categorias.html', {'categorias': categorias})


def agregar_categoria(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        Categoria.objects.create(nombre=nombre)
        return redirect('categorias')
    return render(request, 'agregar_categoria.html')


def editar_categoria(request, id):
    categoria = Categoria.objects.get(pk=id)
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        categoria.nombre = nombre
        categoria.save()
        return redirect('categorias')
    return render(request, 'editar_categoria.html', {'categoria': categoria})


def eliminar_categoria(request, id):
    categoria = Categoria.objects.get(pk=id)
    if request.method == 'POST':
        categoria.delete()
        return redirect('categorias')
    return render(request, 'eliminar_categoria.html', {'categoria': categoria})


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
            return redirect('proveedor_list')
    else:
        form = ProveedorForm()
    return render(request, 'agregar_proveedor.html', {'form': form})


def editar_proveedor(request, proveedor_id):
    proveedor = get_object_or_404(Proveedor, pk=proveedor_id)
    if request.method == 'POST':
        form = ProveedorForm(request.POST, instance=proveedor)
        if form.is_valid():
            form.save()
            return redirect('proveedor_list')
    else:
        form = ProveedorForm(instance=proveedor)
    return render(request, 'editar_proveedor.html', {'form': form})


def borrar_proveedor(request, proveedor_id):
    proveedor = get_object_or_404(Proveedor, pk=proveedor_id)
    if request.method == 'POST':
        proveedor.delete()
        return redirect('proveedor_list')
    return render(request, 'borrar_proveedor.html',
                  {'proveedor': proveedor})


def agregar_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('producto_list')
    else:
        form = ProductoForm()
    return render(request, 'agregar_producto.html', {'form': form})


def editar_producto(request, producto_id):
    producto = get_object_or_404(Producto, pk=producto_id)
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('producto_list')
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'editar_producto.html', {'form': form})


def borrar_producto(request, producto_id):
    producto = get_object_or_404(Producto, pk=producto_id)
    if request.method == 'POST':
        producto.delete()
        return redirect('producto_list')
    return render(request, 'borrar_producto.html', {'producto': producto})
