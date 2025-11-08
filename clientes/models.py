from django.db import models
from django.conf import settings

class Cliente(models.Model):
    usuario = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="perfil_cliente",
        null=True, blank=True
    )
    entrenadores = models.ManyToManyField(
        settings.AUTH_USER_MODEL, 
        related_name="clientes",
        blank=True
    )
    nombre = models.CharField(max_length=100)
    edad = models.PositiveIntegerField(null=True, blank=True)
    altura_cm = models.PositiveIntegerField(null=True, blank=True)
    peso_kg = models.FloatField(null=True, blank=True)
    lesiones = models.TextField(blank=True, help_text="Anotar lesiones o complicaciones")

    def __str__(self):
        return self.nombre
