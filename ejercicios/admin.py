from django.contrib import admin
from .models import Ejercicio
# Register your models here.
@admin.register(Ejercicio)
class EjercicioAdmin(admin.ModelAdmin):
    list_display = ("nombre", "grupo_muscular", "descanso_segundos", "rir", "rpe")
    search_fields = ("nombre", "grupo_muscular")