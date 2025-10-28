# progreso/urls.py
from django.urls import path
from . import views
from .views import (
    ProgresoListaView,
    ProgresoCrearView,
    ProgresoEditarView,
    ProgresoEliminarView,
    # HistorialEjercicioView,
)

app_name = "progreso"

# progreso/urls.py (fragmento)
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:cliente_id>/", ProgresoListaView.as_view(), name="lista"),
    path("<int:cliente_id>/nuevo/", ProgresoCrearView.as_view(), name="nuevo"),
    path("editar/<int:pk>/", ProgresoEditarView.as_view(), name="editar"),
    path("eliminar/<int:pk>/", ProgresoEliminarView.as_view(), name="eliminar"),

    # ejercicios (corregidas)
    path("<int:cliente_id>/ejercicios/", views.lista_progresos_ejercicios, name="lista_progresos_ejercicios"),
    path("<int:cliente_id>/ejercicios/nuevo/", views.crear_progreso_ejercicio, name="crear_progreso_ejercicio"),
    path("<int:cliente_id>/ejercicios/<int:pk>/editar/", views.editar_progreso_ejercicio, name="editar_progreso_ejercicio"),
    path("<int:cliente_id>/ejercicios/<int:pk>/eliminar/", views.eliminar_progreso_ejercicio, name="eliminar_progreso_ejercicio"),
    path("<int:cliente_id>/ejercicios/<int:pk>/duplicar/", views.duplicar_progreso_ejercicio, name="duplicar_progreso_ejercicio"),

    path("registrar/<int:cliente_id>/<int:ejercicio_id>/", views.registrar_progreso, name="registrar"),
    # path("historial/ejercicio/<int:cliente_id>/", HistorialEjercicioView.as_view(), name="historial_ejercicio"),
]

