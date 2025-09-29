from django import forms
from .models import Ejercicio

class EjercicioForm(forms.ModelForm):
    class Meta:
        model = Ejercicio
        fields = ["nombre", "descripcion", "grupo_muscular", "variante"]
        widgets = {
            "nombre": forms.TextInput(attrs={"class": "form-control"}),
            "descripcion": forms.Textarea(attrs={"rows": 3, "class": "form-control"}),
            "grupo_muscular": forms.TextInput(attrs={"class": "form-control"}),
            "variante": forms.TextInput(attrs={"class": "form-control"}),
        }
