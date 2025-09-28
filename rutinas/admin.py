from django.contrib import admin
from .models import Rutina, EntradaEjercicio
# Register your models here.
@admin.register(Rutina)
class RutinaAdmin(admin.ModelAdmin):
    list_display = ("nombre", "cliente", "fecha_creacion")
    search_fields = ("nombre", "cliente__nombre")
    list_filter = ("cliente",)

@admin.register(EntradaEjercicio)
class EntradaEjercicioAdmin(admin.ModelAdmin):
    list_display = ("rutina", "ejercicio", "series", "repeticiones", "peso_kg")
    search_fields = ("rutina__nombre", "ejercicio__nombre")
    list_filter = ("rutina", "ejercicio")
