from django import forms
from .models import Rutina, EntradaEjercicio

class RutinaForm(forms.ModelForm):
    class Meta:
        model = Rutina
        fields = ["nombre", "descripcion", "cliente"]

class EntradaEjercicioForm(forms.ModelForm):
    class Meta:
        model = EntradaEjercicio
        fields = ["ejercicio", "series", "repeticiones", "peso_kg", "descanso_segundos", "rir", "rpe"]
