from django.urls import path
from . import views
from .views import (
    ClienteListaView,
    ClienteDetalleView,
    ClienteCrearView,
    ClienteEditarView,
)
from django.views.generic import DeleteView
from .models import Cliente
from django.urls import reverse_lazy

app_name = "clientes"

urlpatterns = [
    path("", ClienteListaView.as_view(), name="lista"),
    path("<int:pk>/", ClienteDetalleView.as_view(), name="detalle"),
    path("nuevo/", ClienteCrearView.as_view(), name="crear"),
    path("editar/<int:pk>/", ClienteEditarView.as_view(), name="editar"),
    path("eliminar/<int:pk>/", DeleteView.as_view(
        model=Cliente,
        template_name="clientes/confirmar_eliminar.html",
        success_url=reverse_lazy("clientes:lista")
    ), name="eliminar"),
    path("buscar/", views.buscar_clientes, name="buscar"),
    path("buscar/ajax/", views.buscar_clientes_ajax, name="buscar_ajax"),

    path("asignar/<int:cliente_id>/", views.asignar_cliente, name="asignar"),
    path("desasignar/<int:cliente_id>/", views.desasignar_cliente, name="desasignar"),
    
]
