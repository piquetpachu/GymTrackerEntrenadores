from django.db import models

# Create your models here.
from django.db import models
from clientes.models import Cliente

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
