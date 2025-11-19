from django import forms

from clientes.models import Cliente
from .models import Rutina, EntradaEjercicio


class RutinaForm(forms.ModelForm):
    class Meta:
        model = Rutina
        fields = ["cliente", "nombre", "descripcion"]
        widgets = {
            "cliente": forms.Select(attrs={
                "class": "w-full px-4 py-3 bg-gray-700 border border-gray-600 rounded-lg text-white focus:outline-none focus:ring-2 focus:ring-emerald-500 focus:border-transparent transition-colors"
            }),
            "nombre": forms.TextInput(attrs={
                "class": "w-full px-4 py-3 bg-gray-700 border border-gray-600 rounded-lg text-white placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-emerald-500 focus:border-transparent transition-colors",
                "placeholder": "Nombre de la rutina"
            }),
            "descripcion": forms.Textarea(attrs={
                "class": "w-full px-4 py-3 bg-gray-700 border border-gray-600 rounded-lg text-white placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-emerald-500 focus:border-transparent transition-colors",
                "rows": 3,
                "placeholder": "Descripción y objetivos de la rutina"
            }),
        }

    def __init__(self, *args, **kwargs):
        # 👇 Capturamos el usuario actual
        user = kwargs.pop("user", None)
        super().__init__(*args, **kwargs)

        # Etiquetas
        self.fields['cliente'].label = "Cliente *"
        self.fields['nombre'].label = "Nombre de la Rutina *"
        self.fields['descripcion'].label = "Descripción"

        # 👇 Si el usuario es cliente, eliminamos el campo del formulario
        if user and hasattr(user, 'rol') and user.rol == 'cliente':
            self.fields.pop('cliente', None)

            # Si el usuario es cliente → ocultar el campo
        if user and hasattr(user, 'rol') and user.rol == 'cliente':
            self.fields.pop('cliente', None)
    
        # 👇 Si el usuario es entrenador → filtrar sus clientes
        elif user:
            self.fields['cliente'].queryset = Cliente.objects.filter(entrenadores=user)
class EntradaEjercicioForm(forms.ModelForm):
    class Meta:
        model = EntradaEjercicio
        fields = ["ejercicio", "series", "repeticiones", "peso_kg", "descanso_segundos", "rir", "rpe", "notas"]
        widgets = {
            "ejercicio": forms.Select(attrs={
                "class": "w-full px-4 py-3 bg-gray-700 border border-gray-600 rounded-lg text-white focus:outline-none focus:ring-2 focus:ring-emerald-500 focus:border-transparent transition-colors"
            }),
            "series": forms.NumberInput(attrs={
                "class": "w-full px-4 py-3 bg-gray-700 border border-gray-600 rounded-lg text-white placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-emerald-500 focus:border-transparent transition-colors",
                "placeholder": "Ej: 3",
                "min": "1"
            }),
            "repeticiones": forms.NumberInput(attrs={
                "class": "w-full px-4 py-3 bg-gray-700 border border-gray-600 rounded-lg text-white placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-emerald-500 focus:border-transparent transition-colors",
                "placeholder": "Ej: 10",
                "min": "1"
            }),
            "peso_kg": forms.NumberInput(attrs={
                "class": "w-full px-4 py-3 bg-gray-700 border border-gray-600 rounded-lg text-white placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-emerald-500 focus:border-transparent transition-colors",
                "placeholder": "Ej: 20.5",
                "step": "0.5",
                "min": "0"
            }),
            "descanso_segundos": forms.NumberInput(attrs={
                "class": "w-full px-4 py-3 bg-gray-700 border border-gray-600 rounded-lg text-white placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-emerald-500 focus:border-transparent transition-colors",
                "placeholder": "Ej: 90",
                "min": "0"
            }),
            "rir": forms.NumberInput(attrs={
                "class": "w-full px-4 py-3 bg-gray-700 border border-gray-600 rounded-lg text-white placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-emerald-500 focus:border-transparent transition-colors",
                "placeholder": "0-4 (Reps In Reserve)",
                "min": "0",
                "max": "4"
            }),
            "rpe": forms.NumberInput(attrs={
                "class": "w-full px-4 py-3 bg-gray-700 border border-gray-600 rounded-lg text-white placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-emerald-500 focus:border-transparent transition-colors",
                "placeholder": "1-10 (Rate of Perceived Exertion)",
                "min": "1",
                "max": "10"
            }),
            "notas": forms.Textarea(attrs={
                "class": "w-full px-4 py-3 bg-gray-700 border border-gray-600 rounded-lg text-white placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-emerald-500 focus:border-transparent transition-colors",
                "rows": 3,
                "placeholder": "Notas técnicas, variantes, observaciones..."
            }),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Mejorar labels y agregar help texts
        self.fields['ejercicio'].label = "Ejercicio *"
        self.fields['series'].label = "Series"
        self.fields['repeticiones'].label = "Repeticiones"
        self.fields['peso_kg'].label = "Peso (kg)"
        self.fields['descanso_segundos'].label = "Descanso (segundos)"
        self.fields['rir'].label = "RIR"
        self.fields['rpe'].label = "RPE"
        self.fields['notas'].label = "Notas"
        
        # Help texts para métricas avanzadas
        self.fields['rir'].help_text = "Repeticiones en reserva (0-4): cuántas repeticiones más podrías hacer"
        self.fields['rpe'].help_text = "Esfuerzo percibido (1-10): qué tan difícil fue el ejercicio"