from django import forms
from .models import Cliente
from usuarios.models import Usuario

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ["nombre", "edad", "altura_cm", "peso_kg", "lesiones", "entrenadores"]
        widgets = {
            "lesiones": forms.Textarea(attrs={
                "rows": 3, 
                "class": "w-full px-4 py-3 bg-gray-700 border border-gray-600 rounded-lg text-white placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-emerald-500 focus:border-transparent transition-colors",
                "placeholder": "Acotar lesiones o complicaciones"
            }),
            "nombre": forms.TextInput(attrs={
                "class": "w-full px-4 py-3 bg-gray-700 border border-gray-600 rounded-lg text-white placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-emerald-500 focus:border-transparent transition-colors",
                "placeholder": "Nombre completo del cliente"
            }),
            "edad": forms.NumberInput(attrs={
                "class": "w-full px-4 py-3 bg-gray-700 border border-gray-600 rounded-lg text-white placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-emerald-500 focus:border-transparent transition-colors",
                "placeholder": "Edad en años"
            }),
            "altura_cm": forms.NumberInput(attrs={
                "class": "w-full px-4 py-3 bg-gray-700 border border-gray-600 rounded-lg text-white placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-emerald-500 focus:border-transparent transition-colors",
                "placeholder": "Altura en centímetros"
            }),
            "peso_kg": forms.NumberInput(attrs={
                "class": "w-full px-4 py-3 bg-gray-700 border border-gray-600 rounded-lg text-white placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-emerald-500 focus:border-transparent transition-colors",
                "placeholder": "Peso en kilogramos",
                "step": "0.1"
            }),
            "entrenadores": forms.SelectMultiple(attrs={
                "class": "w-full px-4 py-3 bg-gray-700 border border-gray-600 rounded-lg text-white focus:outline-none focus:ring-2 focus:ring-emerald-500 focus:border-transparent transition-colors h-32"
            }),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Solo mostrar usuarios con rol = "entrenador"
        self.fields["entrenadores"].queryset = Usuario.objects.filter(rol="entrenador")
        
        # Agregar placeholders y mejorar labels
        self.fields['nombre'].label = "Nombre *"
        self.fields['edad'].label = "Edad"
        self.fields['altura_cm'].label = "Altura (cm)"
        self.fields['peso_kg'].label = "Peso (kg)"
        self.fields['lesiones'].label = "Lesiones"
        self.fields['entrenadores'].label = "Entrenadores *"