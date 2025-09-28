from django.contrib import admin
from .models import Cliente
# Register your models here.
@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ("nombre", "edad", "altura_cm", "peso_kg")
    search_fields = ("nombre",)
    list_filter = ("entrenadores",)
    filter_horizontal = ("entrenadores",)