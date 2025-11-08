from django.db import models

# Create your models here.
from django.db import models
from clientes.models import Cliente
from ejercicios.models import Ejercicio

from django.db import models
from clientes.models import Cliente
from ejercicios.models import Ejercicio
from usuarios.models import Usuario


class Rutina(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    ejercicios = models.ManyToManyField(Ejercicio, related_name="rutinas")

    entrenador = models.ForeignKey(
        Usuario,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="rutinas_creadas"
    )

    cliente = models.ForeignKey(
        Cliente,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="rutinas"
    )

    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre} ({self.cliente or 'Sin cliente'})"


class EntradaEjercicio(models.Model):
    rutina = models.ForeignKey(Rutina, on_delete=models.CASCADE, related_name="entradas")
    ejercicio = models.ForeignKey(Ejercicio, on_delete=models.CASCADE)
    series = models.PositiveIntegerField()
    repeticiones = models.PositiveIntegerField()
    peso_kg = models.FloatField(null=True, blank=True)
    descanso_segundos = models.PositiveIntegerField(default=60)
    rir = models.PositiveIntegerField(help_text="Repeticiones en reserva", default=1)
    rpe = models.PositiveIntegerField(help_text="Esfuerzo percibido (1-10)", default=9)
    notas = models.TextField(blank=True)

    def __str__(self):
        return f"{self.ejercicio.nombre} ({self.series}x{self.repeticiones})"
