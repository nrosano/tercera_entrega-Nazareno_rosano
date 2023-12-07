from django.shortcuts import render, redirect
from .models import Categoria, Producto, Cliente
from .forms import CategoriaForm, ProductoForm, ClienteForm, ProductoSearchForm

def index(request):
    return render(request, 'index.html')

def categoria_form(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CategoriaForm()
    return render(request, 'categoria_form.html', {'form': form})

def producto_form(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ProductoForm()
    return render(request, 'producto_form.html', {'form': form})

def cliente_form(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ClienteForm()
    return render(request, 'cliente_form.html', {'form': form})

def search_productos(request):
    form = ProductoSearchForm(request.GET)
    productos = None

    if form.is_valid():
        productos = form.filter_productos(Producto.objects.all())

    return render(request, 'search_productos.html', {'form': form, 'productos': productos})
