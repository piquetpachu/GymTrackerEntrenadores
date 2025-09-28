from django.db import models

# Create your models here.
from django.db import models

class Ejercicio(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    grupo_muscular = models.CharField(max_length=100)
    descanso_segundos = models.PositiveIntegerField(default=60)
    rir = models.PositiveIntegerField(help_text="Repeticiones en reserva")
    rpe = models.PositiveIntegerField(help_text="Esfuerzo percibido (1-10)")

    def __str__(self):
        return self.nombre
