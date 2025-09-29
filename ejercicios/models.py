from django.db import models

# Create your models here.
from django.db import models

class Ejercicio(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    grupo_muscular = models.CharField(max_length=100)
    variante = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.nombre
