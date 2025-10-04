from django import forms
from .models import Rutina, EntradaEjercicio

class RutinaForm(forms.ModelForm):
    class Meta:
        model = Rutina
        fields = ["nombre", "descripcion"]
        widgets = {
            "nombre": forms.TextInput(attrs={"class": "form-control"}),
            "descripcion": forms.Textarea(attrs={"class": "form-control", "rows": 3}),
        }

class EntradaEjercicioForm(forms.ModelForm):
    class Meta:
        model = EntradaEjercicio
        fields = ["ejercicio", "series", "repeticiones", "peso_kg", "descanso_segundos", "rir", "rpe", "notas"]
        widgets = {
            "ejercicio": forms.Select(attrs={"class": "form-control"}),
            "series": forms.NumberInput(attrs={"class": "form-control"}),
            "repeticiones": forms.NumberInput(attrs={"class": "form-control"}),
            "peso_kg": forms.NumberInput(attrs={"class": "form-control"}),
            "descanso_segundos": forms.NumberInput(attrs={"class": "form-control"}),
            "rir": forms.NumberInput(attrs={"class": "form-control"}),
            "rpe": forms.NumberInput(attrs={"class": "form-control"}),
            "notas": forms.Textarea(attrs={"class": "form-control", "rows": 3}),
        }