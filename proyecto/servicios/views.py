from django.shortcuts import render, redirect
from .models import Juegos, Promociones, Sorteos
from .forms import JuegosForm, PromocionesForm, SorteosForm
# Create your views here.

def index(request):
    return render(request, 'servicios/index.html')

def juegos_list(request):
    query = Juegos.objects.all()
    context = {"object_list": query}
    return render(request, 'servicios/juegos_list.html', context)

def promociones_list(request):
    query = Promociones.objects.all()
    context = {"object_list": query}
    return render(request, 'servicios/promociones_list.html', context)

def sorteos_list(request):
    query = Sorteos.objects.all()
    context = {"object_list": query}
    return render(request, 'servicios/sorteos_list.html', context)

def juegos_create(request):
    if request.method == 'GET':
        form = JuegosForm()

    if request.method == 'POST':
        form = JuegosForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('juegos_list')

    return render(request, 'servicios/juegos_create.html', { 'form': form })

def promociones_create(request):
    if request.method == 'GET':
        form = PromocionesForm()

    if request.method == 'POST':
        form = PromocionesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('promociones_list')

    return render(request, 'servicios/promociones_create.html' , { 'form': form })

def sorteos_create(request):
    if request.method == 'GET':
        form = SorteosForm()
    if request.method == 'POST':
        form = SorteosForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sorteos_list')
            
    return render(request, 'servicios/sorteos_create.html', { 'form': form })
