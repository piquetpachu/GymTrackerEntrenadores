from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Progreso, ProgresoEjercicio
from ejercicios.models import Ejercicio
from clientes.models import Cliente
from .forms import ProgresoForm, ProgresoEjercicioForm
from django.utils.timezone import now


def index(request):
    clientes = Cliente.objects.all()
    return render(request, "progreso/index.html", {"clientes": clientes})

class ProgresoListaView(ListView):
    model = Progreso
    template_name = "progreso/lista.html"
    context_object_name = "progresos"

    def get_queryset(self):
        cliente = get_object_or_404(Cliente, pk=self.kwargs["cliente_id"])
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


def lista_progresos_ejercicios(request):
    progresos = ProgresoEjercicio.objects.all().order_by("-fecha")
    return render(request, "progreso/ejercicio_list.html", {"progresos": progresos})

def crear_progreso_ejercicio(request):
    if request.method == "POST":
        form = ProgresoEjercicioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("progreso:lista_progresos_ejercicios")
    else:
        form = ProgresoEjercicioForm()
    return render(request, "progreso/ejercicio_form.html", {"form": form})

def editar_progreso_ejercicio(request, pk):
    progreso = get_object_or_404(ProgresoEjercicio, pk=pk)
    if request.method == "POST":
        form = ProgresoEjercicioForm(request.POST, instance=progreso)
        if form.is_valid():
            form.save()
            return redirect("progreso:lista_progresos_ejercicios")
    else:
        form = ProgresoEjercicioForm(instance=progreso)
    return render(request, "progreso/ejercicio_form.html", {"form": form})

def eliminar_progreso_ejercicio(request, pk):
    progreso = get_object_or_404(ProgresoEjercicio, pk=pk)
    if request.method == "POST":
        progreso.delete()
        return redirect("progreso:lista_progresos_ejercicios")
    return render(request, "progreso/ejercicio_confirm_delete.html", {"progreso": progreso})

def registrar_progreso(request, cliente_id, ejercicio_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)
    ejercicio = get_object_or_404(Ejercicio, id=ejercicio_id)

    if request.method == "POST":
        peso = request.POST.get("peso")
        repeticiones = request.POST.get("repeticiones")
        if peso and repeticiones:
            ProgresoEjercicio.objects.create(
                cliente=cliente,
                ejercicio=ejercicio,
                peso=peso,
                repeticiones=repeticiones,
            )
        return redirect("progreso:registrar", cliente_id=cliente.id, ejercicio_id=ejercicio.id)

    progresos = ProgresoEjercicio.objects.filter(cliente=cliente, ejercicio=ejercicio).order_by("-fecha")[:10]
    return render(request, "progreso/registrar.html", {
        "cliente": cliente,
        "ejercicio": ejercicio,
        "progresos": progresos
    })
