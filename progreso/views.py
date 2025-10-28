from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.utils.timezone import now
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Progreso, ProgresoEjercicio
from ejercicios.models import Ejercicio
from clientes.models import Cliente
from .forms import ProgresoForm, ProgresoEjercicioForm
from usuarios.mixins import LoginRequiredCustomMixin, RolRequiredMixin, EntrenadorQuerysetMixin


@login_required
def index(request):
    if request.user.is_superuser:
        clientes = Cliente.objects.all()
    else:
        clientes = Cliente.objects.filter(entrenadores=request.user)
    return render(request, "progreso/index.html", {"clientes": clientes})


class ProgresoListaView(LoginRequiredCustomMixin, RolRequiredMixin, EntrenadorQuerysetMixin, ListView):
    model = Progreso
    template_name = "progreso/lista.html"
    context_object_name = "progresos"
    rol_permitido = "entrenador"  # 👈 solo entrenadores

    def get_queryset(self):
        user = self.request.user
        cliente = get_object_or_404(Cliente, pk=self.kwargs["cliente_id"])
        
        # 🔒 Seguridad: verificamos que el cliente pertenece al entrenador logueado
        if not cliente.entrenadores.filter(id=user.id).exists():
            return Progreso.objects.none()
        
        return Progreso.objects.filter(cliente=cliente)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cliente"] = get_object_or_404(Cliente, pk=self.kwargs["cliente_id"])
        return context

class ProgresoCrearView(CreateView):
    model = Progreso
    form_class = ProgresoForm
    template_name = "progreso/formulario.html"

    def form_valid(self, form):
        cliente = get_object_or_404(Cliente, pk=self.kwargs["cliente_id"])
        form.instance.cliente = cliente
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("progreso:lista", kwargs={"cliente_id": self.kwargs["cliente_id"]})


class ProgresoEditarView(UpdateView):
    model = Progreso
    form_class = ProgresoForm
    template_name = "progreso/formulario.html"

    def get_success_url(self):
        return reverse_lazy("progreso:lista", kwargs={"cliente_id": self.object.cliente.id})


class ProgresoEliminarView(DeleteView):
    model = Progreso
    template_name = "progreso/confirmar_eliminar.html"

    def get_success_url(self):
        return reverse_lazy("progreso:lista", kwargs={"cliente_id": self.object.cliente.id})


def lista_progresos_ejercicios(request, cliente_id):
    cliente = get_object_or_404(Cliente, pk=cliente_id)

    # seguridad: sólo entrenadores del cliente (o superuser) pueden acceder
    if not request.user.is_superuser and not cliente.entrenadores.filter(id=request.user.id).exists():
        return redirect("clientes:lista")

    progresos = ProgresoEjercicio.objects.filter(cliente=cliente).order_by("-fecha")
    return render(request, "progreso/ejercicio_list.html", {
        "cliente": cliente,
        "progresos": progresos
    })


def crear_progreso_ejercicio(request, cliente_id):
    cliente = get_object_or_404(Cliente, pk=cliente_id)

    # seguridad
    if not request.user.is_superuser and not cliente.entrenadores.filter(id=request.user.id).exists():
        return redirect("clientes:lista")

    if request.method == "POST":
        form = ProgresoEjercicioForm(request.POST)
        if form.is_valid():
            progreso = form.save(commit=False)
            progreso.cliente = cliente
            progreso.save()
            messages.success(request, "Progreso creado correctamente.")
            return redirect("progreso:lista_progresos_ejercicios", cliente_id=cliente.id)
    else:
        form = ProgresoEjercicioForm(initial={"cliente": cliente.id})

    return render(request, "progreso/ejercicio_form.html", {"form": form, "cliente": cliente})


def editar_progreso_ejercicio(request, cliente_id, pk):
    cliente = get_object_or_404(Cliente, pk=cliente_id)
    progreso = get_object_or_404(ProgresoEjercicio, pk=pk, cliente=cliente)

    # seguridad
    if not request.user.is_superuser and not cliente.entrenadores.filter(id=request.user.id).exists():
        return redirect("clientes:lista")

    if request.method == "POST":
        form = ProgresoEjercicioForm(request.POST, instance=progreso)
        if form.is_valid():
            form.save()
            messages.success(request, "Progreso actualizado correctamente.")
            return redirect("progreso:lista_progresos_ejercicios", cliente_id=cliente.id)
    else:
        form = ProgresoEjercicioForm(instance=progreso)

    return render(request, "progreso/ejercicio_form.html", {"form": form, "cliente": cliente, "progreso": progreso})


def eliminar_progreso_ejercicio(request, cliente_id, pk):
    cliente = get_object_or_404(Cliente, pk=cliente_id)
    progreso = get_object_or_404(ProgresoEjercicio, pk=pk, cliente=cliente)

    # seguridad
    if not request.user.is_superuser and not cliente.entrenadores.filter(id=request.user.id).exists():
        return redirect("clientes:lista")

    if request.method == "POST":
        progreso.delete()
        messages.success(request, "Progreso eliminado correctamente.")
        return redirect("progreso:lista_progresos_ejercicios", cliente_id=cliente.id)

    return render(request, "progreso/ejercicio_confirm_delete.html", {"progreso": progreso, "cliente": cliente})

from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render

def eliminar_progreso_desde_registrar(request, cliente_id, pk, ejercicio_id):
    """
    Permite eliminar un progreso desde la vista 'registrar progreso'
    y redirige nuevamente a esa misma pantalla.
    """
    cliente = get_object_or_404(Cliente, pk=cliente_id)
    progreso = get_object_or_404(ProgresoEjercicio, pk=pk, cliente=cliente)

    # Seguridad: sólo entrenadores del cliente o superusuarios
    if not request.user.is_superuser and not cliente.entrenadores.filter(id=request.user.id).exists():
        return redirect("clientes:lista")

    if request.method == "POST":
        progreso.delete()
        messages.success(request, "Progreso eliminado correctamente.")
        return redirect("progreso:registrar", cliente_id=cliente.id, ejercicio_id=ejercicio_id)

    # Si alguien entra por GET, mostrar confirmación (opcional)
    return render(
        request,
        "progreso/ejercicio_confirm_delete.html",
        {"progreso": progreso, "cliente": cliente, "volver": f"/progreso/registrar/{cliente.id}/{ejercicio_id}/"},
    )

def registrar_progreso(request, cliente_id, ejercicio_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)
    ejercicio = get_object_or_404(Ejercicio, id=ejercicio_id)

    # seguridad: sólo entrenadores / superuser
    if not request.user.is_superuser and not cliente.entrenadores.filter(id=request.user.id).exists():
        return redirect("clientes:lista")

    if request.method == "POST":
        progreso_id = request.POST.get("progreso_id", "").strip()
        peso = request.POST.get("peso", "").replace(",", ".").strip()
        repeticiones = request.POST.get("repeticiones", "").strip()
        notas = request.POST.get("notas", "").strip()

        # Si viene progreso_id, actualizamos
        if progreso_id:
            progreso = get_object_or_404(ProgresoEjercicio, pk=progreso_id, cliente=cliente, ejercicio=ejercicio)
            if peso != "":
                progreso.peso = peso
            if repeticiones != "":
                try:
                    progreso.repeticiones = int(float(repeticiones))
                except ValueError:
                    progreso.repeticiones = 0

            progreso.notas = notas
            progreso.save()
            messages.success(request, "Progreso actualizado correctamente.")
        else:
            # crear sólo si hay reps o peso (evitamos crear vacíos)
            nuevo = ProgresoEjercicio.objects.create(
                cliente=cliente,
                ejercicio=ejercicio,
                peso=(peso if peso != "" else None),
                repeticiones=(int(float(repeticiones)) if repeticiones != "" else 0),
                notas=notas
            )

            messages.success(request, "Progreso registrado correctamente.")

        return redirect("progreso:registrar", cliente_id=cliente.id, ejercicio_id=ejercicio.id)

    # GET: último y últimos 10 para la plantilla
    ultimo_progreso = ProgresoEjercicio.objects.filter(cliente=cliente, ejercicio=ejercicio).order_by("-fecha").first()
    progresos = ProgresoEjercicio.objects.filter(cliente=cliente, ejercicio=ejercicio).order_by("-fecha")[:10]

    return render(request, "progreso/registrar.html", {
        "cliente": cliente,
        "ejercicio": ejercicio,
        "progresos": progresos,
        "ultimo_progreso": ultimo_progreso,
    })


def duplicar_progreso_ejercicio(request, cliente_id, pk):
    cliente = get_object_or_404(Cliente, pk=cliente_id)
    progreso = get_object_or_404(ProgresoEjercicio, pk=pk, cliente=cliente)

    # seguridad
    if not request.user.is_superuser and not cliente.entrenadores.filter(id=request.user.id).exists():
        return redirect("clientes:lista")

    nuevo_progreso = ProgresoEjercicio.objects.create(
        cliente=progreso.cliente,
        ejercicio=progreso.ejercicio,
        peso=progreso.peso,
        repeticiones=progreso.repeticiones,
        notas=progreso.notas,
        fecha=now().date()
    )
    messages.success(request, "Progreso duplicado correctamente.")
    return redirect("progreso:registrar", cliente_id=progreso.cliente.id, ejercicio_id=progreso.ejercicio.id)