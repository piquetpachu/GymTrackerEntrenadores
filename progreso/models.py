from django.db import models

# Create your models here.
from django.db import models
from clientes.models import Cliente
from rutinas.models import Ejercicio, Rutina


class Progreso(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name="progresos")
    fecha = models.DateField(auto_now_add=True)

    peso_kg = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    altura_cm = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    cintura_cm = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    pecho_cm = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    brazo_cm = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    pierna_cm = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)

    notas = models.TextField(blank=True)

    class Meta:
        ordering = ["-fecha"]

    def __str__(self):
        return f"Progreso de {self.cliente.nombre} - {self.fecha}"


class ProgresoEjercicio(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name="progresos_ejercicios")
    rutina = models.ForeignKey(Rutina, on_delete=models.CASCADE, related_name="progresos_ejercicios", null=True, blank=True)
    ejercicio = models.ForeignKey(Ejercicio, on_delete=models.CASCADE)
    fecha = models.DateField(auto_now_add=True)

    series = models.PositiveIntegerField(default=1)
    repeticiones = models.PositiveIntegerField()
    peso = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)  # kg usados
    notas = models.TextField(blank=True)
    rir = models.PositiveIntegerField(
        null=True, blank=True,
        help_text="Repeticiones en reserva (0-5 aprox)"
    )
    rpe = models.PositiveIntegerField(
        null=True, blank=True,
        help_text="Esfuerzo percibido (1-10)"
    )

    class Meta:
        ordering = ["-fecha"]

    def __str__(self):
        return f"{self.ejercicio.nombre} - {self.repeticiones} reps @ {self.peso}kg ({self.fecha})"
