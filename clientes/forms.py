from django import forms
from .models import Cliente
from usuarios.models import Usuario

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ["nombre", "edad", "altura_cm", "peso_kg", "lesiones", "entrenadores"]
        widgets = {
            "lesiones": forms.Textarea(attrs={"rows": 3, "class": "form-control"}),
            "nombre": forms.TextInput(attrs={"class": "form-control"}),
            "edad": forms.NumberInput(attrs={"class": "form-control"}),
            "altura_cm": forms.NumberInput(attrs={"class": "form-control"}),
            "peso_kg": forms.NumberInput(attrs={"class": "form-control"}),
            "entrenadores": forms.SelectMultiple(attrs={"class": "form-control"}),
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Solo mostrar usuarios con rol = "entrenador"
        self.fields["entrenadores"].queryset = Usuario.objects.filter(rol="entrenador")