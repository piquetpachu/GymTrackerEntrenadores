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
            "peso_kg": forms.NumberInput(attrs={
                "class": "w-full px-4 py-3 bg-gray-700 border border-gray-600 rounded-lg text-white placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-emerald-500 focus:border-transparent transition-colors",
                "placeholder": "Peso en kilogramos",
                "step": "0.1",
                "min": "0"
            }),
            "altura_cm": forms.NumberInput(attrs={
                "class": "w-full px-4 py-3 bg-gray-700 border border-gray-600 rounded-lg text-white placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-emerald-500 focus:border-transparent transition-colors",
                "placeholder": "Altura en centímetros",
                "min": "0"
            }),
            "cintura_cm": forms.NumberInput(attrs={
                "class": "w-full px-4 py-3 bg-gray-700 border border-gray-600 rounded-lg text-white placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-emerald-500 focus:border-transparent transition-colors",
                "placeholder": "Circunferencia de cintura",
                "step": "0.1",
                "min": "0"
            }),
            "pecho_cm": forms.NumberInput(attrs={
                "class": "w-full px-4 py-3 bg-gray-700 border border-gray-600 rounded-lg text-white placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-emerald-500 focus:border-transparent transition-colors",
                "placeholder": "Circunferencia de pecho",
                "step": "0.1",
                "min": "0"
            }),
            "brazo_cm": forms.NumberInput(attrs={
                "class": "w-full px-4 py-3 bg-gray-700 border border-gray-600 rounded-lg text-white placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-emerald-500 focus:border-transparent transition-colors",
                "placeholder": "Circunferencia de brazo",
                "step": "0.1",
                "min": "0"
            }),
            "pierna_cm": forms.NumberInput(attrs={
                "class": "w-full px-4 py-3 bg-gray-700 border border-gray-600 rounded-lg text-white placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-emerald-500 focus:border-transparent transition-colors",
                "placeholder": "Circunferencia de pierna",
                "step": "0.1",
                "min": "0"
            }),
            "notas": forms.Textarea(attrs={
                "class": "w-full px-4 py-3 bg-gray-700 border border-gray-600 rounded-lg text-white placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-emerald-500 focus:border-transparent transition-colors",
                "rows": 3,
                "placeholder": "Observaciones, comentarios, estado físico..."
            }),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Mejorar labels
        self.fields['peso_kg'].label = "Peso (kg) *"
        self.fields['altura_cm'].label = "Altura (cm)"
        self.fields['cintura_cm'].label = "Cintura (cm)"
        self.fields['pecho_cm'].label = "Pecho (cm)"
        self.fields['brazo_cm'].label = "Brazo (cm)"
        self.fields['pierna_cm'].label = "Pierna (cm)"
        self.fields['notas'].label = "Notas"


class ProgresoEjercicioForm(forms.ModelForm):
    class Meta:
        model = ProgresoEjercicio
        fields = ["cliente", "rutina", "ejercicio", "series", "repeticiones", "peso", "notas"]
        widgets = {
            "cliente": forms.Select(attrs={
                "class": "w-full px-4 py-3 bg-gray-700 border border-gray-600 rounded-lg text-white focus:outline-none focus:ring-2 focus:ring-emerald-500 focus:border-transparent transition-colors"
            }),
            "rutina": forms.Select(attrs={
                "class": "w-full px-4 py-3 bg-gray-700 border border-gray-600 rounded-lg text-white focus:outline-none focus:ring-2 focus:ring-emerald-500 focus:border-transparent transition-colors"
            }),
            "ejercicio": forms.Select(attrs={
                "class": "w-full px-4 py-3 bg-gray-700 border border-gray-600 rounded-lg text-white focus:outline-none focus:ring-2 focus:ring-emerald-500 focus:border-transparent transition-colors"
            }),
            "series": forms.NumberInput(attrs={
                "class": "w-full px-4 py-3 bg-gray-700 border border-gray-600 rounded-lg text-white placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-emerald-500 focus:border-transparent transition-colors",
                "placeholder": "Número de series",
                "min": "1"
            }),
            "repeticiones": forms.NumberInput(attrs={
                "class": "w-full px-4 py-3 bg-gray-700 border border-gray-600 rounded-lg text-white placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-emerald-500 focus:border-transparent transition-colors",
                "placeholder": "Repeticiones por serie",
                "min": "1"
            }),
            "peso": forms.NumberInput(attrs={
                "class": "w-full px-4 py-3 bg-gray-700 border border-gray-600 rounded-lg text-white placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-emerald-500 focus:border-transparent transition-colors",
                "placeholder": "Peso en kilogramos",
                "step": "0.5",
                "min": "0"
            }),
            "notas": forms.Textarea(attrs={
                "class": "w-full px-4 py-3 bg-gray-700 border border-gray-600 rounded-lg text-white placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-emerald-500 focus:border-transparent transition-colors",
                "rows": 3,
                "placeholder": "Notas sobre el ejercicio, técnica, dificultad..."
            }),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Mejorar labels
        self.fields['cliente'].label = "Cliente *"
        self.fields['rutina'].label = "Rutina"
        self.fields['ejercicio'].label = "Ejercicio *"
        self.fields['series'].label = "Series"
        self.fields['repeticiones'].label = "Repeticiones"
        self.fields['peso'].label = "Peso (kg)"
        self.fields['notas'].label = "Notas"