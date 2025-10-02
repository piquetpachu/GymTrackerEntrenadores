from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.urls import reverse_lazy
from .models import Cliente
from .forms import ClienteForm
from django.contrib.auth.decorators import login_required
from usuarios.mixins import LoginRequiredCustomMixin, RolRequiredMixin, EntrenadorQuerysetMixin

class ClienteListaView(LoginRequiredCustomMixin, RolRequiredMixin, EntrenadorQuerysetMixin, ListView):
    model = Cliente
    template_name = "clientes/lista.html"
    context_object_name = "clientes"
    rol_permitido = "entrenador"  # 👈 solo entrenadores


class ClienteDetalleView(DetailView):
    model = Cliente
    template_name = "clientes/detalle.html"
    context_object_name = "cliente"

class ClienteCrearView(CreateView):
    model = Cliente
    form_class = ClienteForm
    template_name = "clientes/formulario.html"
    success_url = reverse_lazy("clientes:lista")

class ClienteEditarView(UpdateView):
    model = Cliente
    form_class = ClienteForm
    template_name = "clientes/formulario.html"
    success_url = reverse_lazy("clientes:lista")




