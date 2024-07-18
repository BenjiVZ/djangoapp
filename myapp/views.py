from django.shortcuts import render
from django.contrib import messages
from myapp.models import Producto

# Create your views here.

def home(request):
    productos_tendencia = Producto.objects.filter(tendencia=True)
    productos_populares = Producto.objects.filter(popular=True)
    data = {
        'tendencia': productos_tendencia,
        'populares': productos_populares
    }
    return render(request, 'home.html')