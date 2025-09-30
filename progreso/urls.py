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

    path("ejercicios/", views.lista_progresos_ejercicios, name="lista_progresos_ejercicios"),
    path("ejercicios/nuevo/", views.crear_progreso_ejercicio, name="crear_progreso_ejercicio"),
    path("ejercicios/<int:pk>/editar/", views.editar_progreso_ejercicio, name="editar_progreso_ejercicio"),
    path("ejercicios/<int:pk>/eliminar/", views.eliminar_progreso_ejercicio, name="eliminar_progreso_ejercicio"),
]
