from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.urls import reverse_lazy
from .models import Cliente

class ClienteListaView(ListView):
    model = Cliente
    template_name = "clientes/lista.html"
    context_object_name = "clientes"

class ClienteDetalleView(DetailView):
    model = Cliente
    template_name = "clientes/detalle.html"
    context_object_name = "cliente"

class ClienteCrearView(CreateView):
    model = Cliente
    template_name = "clientes/formulario.html"
    fields = ["nombre", "edad", "altura_cm", "peso_kg", "lesiones", "entrenadores"]
    success_url = reverse_lazy("clientes:lista")

class ClienteEditarView(UpdateView):
    model = Cliente
    template_name = "clientes/formulario.html"
    fields = ["nombre", "edad", "altura_cm", "peso_kg", "lesiones", "entrenadores"]
    success_url = reverse_lazy("clientes:lista")
