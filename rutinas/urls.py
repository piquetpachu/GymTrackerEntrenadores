from django.urls import path
from . import views
from .views import (
    RutinaListaView, RutinaDetalleView, RutinaCrearView,
    RutinaEditarView, RutinaEliminarView,
    EntradaCrearView, EntradaEditarView, EntradaEliminarView,
)

app_name = "rutinas"

urlpatterns = [
    path("", RutinaListaView.as_view(), name="lista"),
    path("<int:pk>/", RutinaDetalleView.as_view(), name="detalle"),
    path("nueva/", RutinaCrearView.as_view(), name="crear"),
    path("editar/<int:pk>/", RutinaEditarView.as_view(), name="editar"),
    path("eliminar/<int:pk>/", RutinaEliminarView.as_view(), name="eliminar"),
    
    path("<int:rutina_id>/", views.rutina_detalle, name="rutina_detalle"),

    # entradas de ejercicios en la rutina
    path("<int:rutina_id>/entradas/nueva/", EntradaCrearView.as_view(), name="entrada_crear"),
    path("entradas/<int:pk>/editar/", EntradaEditarView.as_view(), name="entrada_editar"),
    path("entradas/<int:pk>/eliminar/", EntradaEliminarView.as_view(), name="entrada_eliminar"),
]
