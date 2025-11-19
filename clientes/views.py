from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.urls import reverse_lazy
from .models import Cliente
from .forms import ClienteForm
from django.contrib.auth.decorators import login_required
from usuarios.mixins import LoginRequiredCustomMixin, RolRequiredMixin, EntrenadorQuerysetMixin
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect,render
from django.contrib import messages

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



@login_required
def buscar_clientes(request):
    entrenador = request.user
    query = request.GET.get("q", "").strip()

    # Todos los clientes del sistema
    clientes = Cliente.objects.all()

    if query:
        clientes = clientes.filter(
            Q(nombre__icontains=query) |
            Q(apellido__icontains=query) |
            Q(email__icontains=query) |
            Q(telefono__icontains=query)
        )

    # Para saber si ya es alumno del entrenador
    clientes_asignados = set(entrenador.clientes.values_list("id", flat=True))

    return render(request, "clientes/buscar.html", {
        "clientes": clientes,
        "query": query,
        "clientes_asignados": clientes_asignados,
    })

@login_required
def asignar_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)
    entrenador = request.user

    cliente.entrenadores.add(entrenador)
    messages.success(request, f"{cliente.nombre} fue agregado a tus clientes.")

    return redirect("clientes:buscar")

@login_required
def desasignar_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)
    entrenador = request.user

    cliente.entrenadores.remove(entrenador)
    messages.success(request, f"{cliente.nombre} fue removido de tus clientes.")

    return redirect("clientes:lista")
