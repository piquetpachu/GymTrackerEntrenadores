from django.db import models
from django.conf import settings

class Ejercicio(models.Model):
    VISIBILIDAD_OPCIONES = [
        ('privado', 'Privado'),
        ('global', 'Global'),
    ]

    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    grupo_muscular = models.CharField(max_length=100)
    variante = models.CharField(max_length=100, blank=True)
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="ejercicios")
    visibilidad = models.CharField(
        max_length=10,
        choices=VISIBILIDAD_OPCIONES,
        default='privado'  # 👈 por defecto será solo visible para su creador
    )

    def __str__(self):
        return self.nombre
