from django.urls import path
from .views import ClienteListaView, ClienteDetalleView, ClienteCrearView, ClienteEditarView

app_name = "clientes"

urlpatterns = [
    path("", ClienteListaView.as_view(), name="lista"),
    path("<int:pk>/", ClienteDetalleView.as_view(), name="detalle"),
    path("crear/", ClienteCrearView.as_view(), name="crear"),
    path("<int:pk>/editar/", ClienteEditarView.as_view(), name="editar"),
]
