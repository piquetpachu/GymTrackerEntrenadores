from django.urls import path
from . import views

app_name = "panel_cliente"

urlpatterns = [
    path("dashboard/", views.dashboard_cliente, name="dashboard"),
    path("rutinas/", views.mis_rutinas, name="rutinas"),
    path("registrar/<int:ejercicio_id>/", views.registrar_progreso_cliente, name="registrar"),
    path("rutinas/crear/", views.crear_rutina_cliente, name="crear_rutina"),
    path("rutinas/<int:rutina_id>/", views.detalle_rutina_cliente, name="detalle_rutina"),
    path("rutinas/<int:rutina_id>/editar/", views.editar_rutina_cliente, name="editar_rutina"),
    path("rutinas/<int:rutina_id>/eliminar/", views.eliminar_rutina_cliente, name="eliminar_rutina"),
    
]
