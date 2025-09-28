from django.http import HttpResponse
from django.test import TestCase
from .models import Ejercicio
# Create your tests here.
def index(request):
    return HttpResponse("Hello, world. You're at the ejercicios index.")

class EjercicioModelTests(TestCase):

    def test_string_representation(self):
        ejercicio = Ejercicio(nombre="Push Up")
        self.assertEqual(str(ejercicio), ejercicio.nombre)
    def test_default_descanso(self):
        ejercicio = Ejercicio(nombre="Squat", descripcion="Leg exercise", grupo_muscular="Legs", rir=2, rpe=7)
        self.assertEqual(ejercicio.descanso_segundos, 60)