from django.shortcuts import render

# Create your views here.
# myapp/views.py

from django.shortcuts import render

def home(request):
    return render(request, 'home.html')