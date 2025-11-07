from django.urls import path
from . import views

app_name = "panel_cliente"

urlpatterns = [
    path("dashboard/", views.dashboard_cliente, name="dashboard"),
    path("rutinas/", views.mis_rutinas, name="rutinas"),
    path("registrar/<int:ejercicio_id>/", views.registrar_progreso_cliente, name="registrar"),
]
