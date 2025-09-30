from django.urls import path
from . import views

app_name = "exportaciones"

urlpatterns = [
    path("progreso/<int:cliente_id>/excel/", views.exportar_progreso_excel, name="progreso_excel"),
    path("rutina/<int:rutina_id>/excel/", views.exportar_rutina_excel, name="rutina_excel"),

]
