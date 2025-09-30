from django import forms
from .models import Progreso, ProgresoEjercicio

class ProgresoForm(forms.ModelForm):
    class Meta:
        model = Progreso
        fields = [
            "peso_kg",
            "altura_cm",
            "cintura_cm",
            "pecho_cm",
            "brazo_cm",
            "pierna_cm",
            "notas",
        ]
        widgets = {
            "peso_kg": forms.NumberInput(attrs={"class": "form-control"}),
            "altura_cm": forms.NumberInput(attrs={"class": "form-control"}),
            "cintura_cm": forms.NumberInput(attrs={"class": "form-control"}),
            "pecho_cm": forms.NumberInput(attrs={"class": "form-control"}),
            "brazo_cm": forms.NumberInput(attrs={"class": "form-control"}),
            "pierna_cm": forms.NumberInput(attrs={"class": "form-control"}),
            "notas": forms.Textarea(attrs={"class": "form-control", "rows": 3}),
        }


class ProgresoEjercicioForm(forms.ModelForm):
    class Meta:
        model = ProgresoEjercicio
        fields = ["cliente", "rutina", "ejercicio", "series", "repeticiones", "peso", "notas"]
