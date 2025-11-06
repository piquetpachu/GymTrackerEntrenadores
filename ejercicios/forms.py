from django import forms
from .models import Ejercicio

class EjercicioForm(forms.ModelForm):
    class Meta:
        model = Ejercicio
        fields = ["nombre", "descripcion", "grupo_muscular", "variante"]
        widgets = {
            "nombre": forms.TextInput(attrs={
                "class": "w-full px-4 py-3 bg-gray-700 border border-gray-600 rounded-lg text-white placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-emerald-500 focus:border-transparent transition-colors",
                "placeholder": "Nombre del ejercicio"
            }),
            "descripcion": forms.Textarea(attrs={
                "rows": 3, 
                "class": "w-full px-4 py-3 bg-gray-700 border border-gray-600 rounded-lg text-white placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-emerald-500 focus:border-transparent transition-colors",
                "placeholder": "Descripción técnica del ejercicio"
            }),
            "grupo_muscular": forms.TextInput(attrs={
                "class": "w-full px-4 py-3 bg-gray-700 border border-gray-600 rounded-lg text-white placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-emerald-500 focus:border-transparent transition-colors",
                "placeholder": "Ej: Pecho, Piernas, Espalda, Hombros"
            }),
            "variante": forms.TextInput(attrs={
                "class": "w-full px-4 py-3 bg-gray-700 border border-gray-600 rounded-lg text-white placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-emerald-500 focus:border-transparent transition-colors",
                "placeholder": "Ej: Con mancuernas, En máquina, Con barra"
            }),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Mejorar labels si lo deseas
        self.fields['nombre'].label = "Nombre del Ejercicio *"
        self.fields['descripcion'].label = "Descripción"
        self.fields['grupo_muscular'].label = "Grupo Muscular"
        self.fields['variante'].label = "Variante"