from django.urls import path
from . import views

app_name = "usuarios"

urlpatterns = [
    path("logout/", views.logout_view, name="logout"),
    path("panel/entrenador/", views.panel_entrenador, name="panel_entrenador"),
    path("panel/admin/", views.panel_admin, name="panel_admin"),
]
