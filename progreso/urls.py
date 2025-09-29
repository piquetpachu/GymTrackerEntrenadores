from django.urls import path
from . import views
from .views import (
    index,
    ProgresoListaView,
    ProgresoCrearView,
    ProgresoEditarView,
    ProgresoEliminarView,
)

app_name = "progreso"

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:cliente_id>/", ProgresoListaView.as_view(), name="lista"),
    path("<int:cliente_id>/nuevo/", ProgresoCrearView.as_view(), name="nuevo"),
    path("editar/<int:pk>/", ProgresoEditarView.as_view(), name="editar"),
    path("eliminar/<int:pk>/", ProgresoEliminarView.as_view(), name="eliminar"),
]
