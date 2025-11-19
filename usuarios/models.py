from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    ROLES = [
        ("admin", "Administrador"),
        ("entrenador", "Entrenador"),
        ("cliente", "Cliente"),
    ]
    
    # Por defecto al registrar un usuario será 'entrenador' (temporal)
    rol = models.CharField(max_length=20, choices=ROLES, default="entrenador")

    def __str__(self):
        return f"{self.username} ({self.rol})"
