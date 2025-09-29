from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Progreso
from clientes.models import Cliente
from .forms import ProgresoForm


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
