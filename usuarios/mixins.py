from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# ✅ Obliga a que el usuario esté logueado
class LoginRequiredCustomMixin(LoginRequiredMixin):
    login_url = "/usuarios/login/"
    login_redirect_url = '/'   # A dónde mandar al usuario después de loguearse
    logout_redirect_url = '/'  # A dónde mandar al usuario después de hacer logout

    redirect_field_name = "next"


# ✅ Solo permite acceso a usuarios con un rol específico
class RolRequiredMixin(UserPassesTestMixin):
    rol_permitido = None  # se define en la vista

    def test_func(self):
        user = self.request.user
        if not user.is_authenticated:
            return False
        if self.rol_permitido:
            return user.rol == self.rol_permitido
        return False


# ✅ Filtra automáticamente los querysets por rol/entrenador
class EntrenadorQuerysetMixin:
    """
    Filtra los objetos para que un entrenador solo vea
    a sus clientes o progresos asociados.
    - Si el usuario es superuser, ve todo.
    - Si es entrenador, filtra por relaciones.
    """

    def get_queryset(self):
        qs = super().get_queryset()
        user = self.request.user

        if user.is_superuser:
            return qs

        # Para modelos que tienen cliente con entrenadores (ej: Progreso)
        if hasattr(self.model, "cliente"):
            return qs.filter(cliente__entrenadores=user)

        # Para modelos que tienen entrenadores directamente (ej: Cliente)
        if hasattr(self.model, "entrenadores"):
            return qs.filter(entrenadores=user)

        return qs.none()
