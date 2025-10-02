from django.contrib import admin
from .models import Usuario
from django.contrib.auth.admin import UserAdmin

# Register your models here.


@admin.register(Usuario)
class UsuarioAdmin(UserAdmin):
    # Mostrar el campo rol en el panel de edición
    fieldsets = UserAdmin.fieldsets + (
        ("Rol", {"fields": ("rol",)}),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Rol", {"fields": ("rol",)}),
    )