from django.shortcuts import render
from .models import Ejercicio
# Create your views here.
def index(request):
    ejercicios = Ejercicio.objects.all()
    return render(request, 'ejercicios/index.html', {'ejercicios': ejercicios})

