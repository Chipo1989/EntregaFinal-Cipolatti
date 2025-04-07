from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import TareaForm, StockForm
from .models import Tarea, Stock

def inicio(request):
    return render(request, 'inicio.html')

def acerca(request):
    return render(request, 'acerca.html')

@login_required
def lista_tareas(request):
    return render(request, 'tareas-lista.html')

@login_required
def lista_stock(request):
    return render(request, 'stock-lista.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

#CRUD tareas

@login_required
def lista_tareas(request):
    tareas = Tarea.objects.filter(usuario=request.user)
    return render(request, 'tareas-lista.html', {'tareas': tareas})

@login_required
def crear_tarea(request):
    if request.method == 'POST':
        form = TareaForm(request.POST)
        if form.is_valid():
            tarea = form.save(commit=False)
            tarea.usuario = request.user
            tarea.save()
            return redirect('tareas')
    else:
        form = TareaForm()
    return render(request, 'tareas-formulario.html', {'form': form})

@login_required
def editar_tarea(request, pk):
    tarea = Tarea.objects.get(pk=pk, usuario=request.user)
    if request.method == 'POST':
        form = TareaForm(request.POST, instance=tarea)
        if form.is_valid():
            form.save()
            return redirect('tareas')
    else:
        form = TareaForm(instance=tarea)
    return render(request, 'tareas-formulario.html', {'form': form})

@login_required
def eliminar_tarea(request, pk):
    tarea = Tarea.objects.get(pk=pk, usuario=request.user)
    if request.method == 'POST':
        tarea.delete()
        return redirect('tareas')
    return render(request, 'tareas-eliminar.html', {'tarea': tarea})


#CRUD stock
@login_required
def lista_stock(request):
    stocks = Stock.objects.filter(usuario=request.user)
    return render(request, 'stock-lista.html', {'stocks': stocks})

@login_required
def crear_stock(request):
    if request.method == 'POST':
        form = StockForm(request.POST)
        if form.is_valid():
            stock = form.save(commit=False)
            stock.usuario = request.user
            stock.save()
            return redirect('stock')
    else:
        form = StockForm()
    return render(request, 'stock-formulario.html', {'form': form})

@login_required
def editar_stock(request, pk):
    stock = Stock.objects.get(pk=pk, usuario=request.user)
    if request.method == 'POST':
        form = StockForm(request.POST, instance=stock)
        if form.is_valid():
            form.save()
            return redirect('stock')
    else:
        form = StockForm(instance=stock)
    return render(request, 'stock-formulario.html', {'form': form})

@login_required
def eliminar_stock(request, pk):
    stock = Stock.objects.get(pk=pk, usuario=request.user)
    if request.method == 'POST':
        stock.delete()
        return redirect('stock')
    return render(request, 'stock-eliminar.html', {'stock': stock})
