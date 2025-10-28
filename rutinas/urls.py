from django.urls import path
from . import views
from .views import (
    RutinaListaView, RutinaDetalleView, RutinaCrearView,
    RutinaEditarView, RutinaEliminarView,
    EntradaCrearView, EntradaEditarView, EntradaEliminarView,
    RutinaCrearParaClienteView, RutinaEditarParaClienteView,RutinaEliminarParaClienteView
)

app_name = "rutinas"

urlpatterns = [
    path("", RutinaListaView.as_view(), name="lista"),
    path("<int:pk>/", RutinaDetalleView.as_view(), name="detalle"),
    path("nueva/", RutinaCrearView.as_view(), name="crear"),
    path("editar/<int:pk>/", RutinaEditarView.as_view(), name="editar"),
    path("eliminar/<int:pk>/", RutinaEliminarView.as_view(), name="eliminar"),

    path("nuevo/<int:cliente_id>/", RutinaCrearParaClienteView.as_view(), name="crear_para_cliente"),
    path("editar/<int:cliente_id>/<int:pk>/", RutinaEditarParaClienteView.as_view(), name="editar_para_cliente"),
    path("eliminar/<int:cliente_id>/<int:pk>/", RutinaEliminarParaClienteView.as_view(), name="eliminar_para_cliente"),
    
    path("<int:rutina_id>/", views.rutina_detalle, name="rutina_detalle"),
    path('cliente/<int:cliente_id>/', views.rutinas_cliente, name='rutinas_cliente'),


    # entradas de ejercicios en la rutina
    path("<int:rutina_id>/entradas/nueva/", EntradaCrearView.as_view(), name="entrada_crear"),
    path("entradas/<int:pk>/editar/", EntradaEditarView.as_view(), name="entrada_editar"),
    path("entradas/<int:pk>/eliminar/", EntradaEliminarView.as_view(), name="entrada_eliminar"),
]
