# usuarios/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario

class RegistroForm(UserCreationForm):
    class Meta:
        model = Usuario
        # No mostramos 'rol' en el formulario de registro; el modelo usa 'entrenador' por defecto
        fields = ["username", "email", "password1", "password2"]
