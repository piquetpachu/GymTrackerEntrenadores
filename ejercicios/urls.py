from django.urls import path
from .views import (
    EjercicioListaView,
    EjercicioDetalleView,
    EjercicioCrearView,
    EjercicioEditarView,
    EjercicioEliminarView,
)

app_name = "ejercicios"

urlpatterns = [
    path("", EjercicioListaView.as_view(), name="lista"),
    path("<int:pk>/", EjercicioDetalleView.as_view(), name="detalle"),
    path("nuevo/", EjercicioCrearView.as_view(), name="crear"),
    path("editar/<int:pk>/", EjercicioEditarView.as_view(), name="editar"),
    path("eliminar/<int:pk>/", EjercicioEliminarView.as_view(), name="eliminar"),
]
