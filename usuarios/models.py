from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    ROLES = (
        ("entrenador", "Entrenador"),
        ("admin", "Administrador"),
    )
    rol = models.CharField(max_length=20, choices=ROLES, default="entrenador")

    def __str__(self):
        return f"{self.username} ({self.rol})"

