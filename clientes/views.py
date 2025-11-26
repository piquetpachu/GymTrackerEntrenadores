from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.urls import reverse_lazy
from .models import Cliente
from .forms import ClienteForm
from django.contrib.auth.decorators import login_required
from usuarios.mixins import LoginRequiredCustomMixin, RolRequiredMixin, EntrenadorQuerysetMixin
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect,render
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

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

    # Base: todos los clientes
    clientes_qs = Cliente.objects.all().order_by("nombre")

    # Filtrado backend (opcional)
    if query:
        palabras = query.split()
        for palabra in palabras:
            clientes_qs = clientes_qs.filter(
                Q(nombre__icontains=palabra) |
                Q(usuario__email__icontains=palabra)
            )

    # Clientes asignados
    clientes_asignados = set(entrenador.clientes.values_list("id", flat=True))

    return render(request, "clientes/buscar.html", {
        "clientes": clientes_qs,  # 👈 SIN paginación
        "query": query,
        "clientes_asignados": clientes_asignados,
    })

from django.http import JsonResponse

@login_required
def buscar_clientes_ajax(request):
    query = request.GET.get("q", "").strip()
    clientes_qs = Cliente.objects.all()

    if query:
        palabras = query.split()
        for palabra in palabras:
            clientes_qs = clientes_qs.filter(
                Q(nombre__icontains=palabra) |
                Q(usuario__email__icontains=palabra) |
                Q(usuario__tel_cel__icontains=palabra)
            )

    resultados = [
        {
            "id": c.id,
            "nombre": c.nombre,
            "email": getattr(c.usuario, "email", "-"),
        }
        for c in clientes_qs[:8]  # máximo 8 resultados
    ]

    return JsonResponse({"resultados": resultados})


@login_required
def asignar_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)
    entrenador = request.user
    cliente.entrenadores.add(entrenador)
    messages.success(request, f"{cliente.nombre} fue agregado a tus clientes.")
    next_url = request.GET.get("next")
    if next_url:
        return redirect(next_url)
    return redirect("clientes:lista")

@login_required
def desasignar_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)
    entrenador = request.user
    cliente.entrenadores.remove(entrenador)
    messages.success(request, f"{cliente.nombre} fue removido de tus clientes.")
    next_url = request.GET.get("next")
    if next_url:
        return redirect(next_url)
    return redirect("clientes:lista")
