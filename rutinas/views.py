from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Rutina, EntradaEjercicio
from clientes.models import Cliente
from .forms import RutinaForm, EntradaEjercicioForm
from django.shortcuts import render, get_object_or_404

# CRUD de Rutinas
class RutinaListaView(ListView):
    model = Rutina
    template_name = "rutinas/lista.html"
    context_object_name = "rutinas"

class RutinaDetalleView(DetailView):
    model = Rutina
    template_name = "rutinas/detalle.html"
    context_object_name = "rutina"

class RutinaCrearView(CreateView):
    model = Rutina
    form_class = RutinaForm
    template_name = "rutinas/formulario.html"
    success_url = reverse_lazy("rutinas:lista")

class RutinaEditarView(UpdateView):
    model = Rutina
    form_class = RutinaForm
    template_name = "rutinas/formulario.html"
    success_url = reverse_lazy("rutinas:lista")

class RutinaEliminarView(DeleteView):
    model = Rutina
    template_name = "rutinas/confirmar_eliminar.html"
    success_url = reverse_lazy("rutinas:lista")

from django.shortcuts import get_object_or_404
from .models import Rutina, EntradaEjercicio

class EntradaCrearView(CreateView):
    model = EntradaEjercicio
    form_class = EntradaEjercicioForm
    template_name = "rutinas/entrada_formulario.html"

    def form_valid(self, form):
        rutina = get_object_or_404(Rutina, pk=self.kwargs["rutina_id"])
        form.instance.rutina = rutina
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("rutinas:detalle", kwargs={"pk": self.kwargs["rutina_id"]})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["rutina_id"] = self.kwargs["rutina_id"]  # 👉 Pasamos el id de la rutina
        return context

class EntradaEditarView(UpdateView):
    model = EntradaEjercicio
    form_class = EntradaEjercicioForm
    template_name = "rutinas/entrada_formulario.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        entrada = self.get_object()
        context["rutina_id"] = entrada.rutina.id   # 👉 pasamos la rutina al template
        return context

    def get_success_url(self):
        return reverse_lazy("rutinas:detalle", kwargs={"pk": self.object.rutina.id})


class EntradaEliminarView(DeleteView):
    model = EntradaEjercicio
    template_name = "rutinas/entrada_confirmar_eliminar.html"

    def get_success_url(self):
        return reverse_lazy("rutinas:detalle", kwargs={"rutina_id": self.object.rutina.pk})


def rutina_detalle(request, rutina_id):
    rutina = get_object_or_404(Rutina, id=rutina_id)
    ejercicios = rutina.ejerciciorutina_set.all()  # suponiendo relación intermedia
    return render(request, "rutinas/detalle.html", {
        "rutina": rutina,
        "ejercicios": ejercicios
    })

class RutinaCrearParaClienteView(CreateView):
    model = Rutina
    form_class = RutinaForm
    template_name = "rutinas/formulario.html"

    def dispatch(self, request, *args, **kwargs):
        self.cliente = get_object_or_404(Cliente, pk=self.kwargs["cliente_id"])
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        rutina = form.save(commit=False)
        rutina.cliente = self.cliente   # 👉 asignamos el cliente automáticamente
        rutina.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("clientes:detalle", kwargs={"pk": self.cliente.id})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cliente"] = self.cliente
        return context
    


class RutinaEditarParaClienteView(UpdateView):
    model = Rutina
    form_class = RutinaForm
    template_name = "rutinas/formulario.html"

    def dispatch(self, request, *args, **kwargs):
        self.cliente = get_object_or_404(Cliente, pk=self.kwargs["cliente_id"])
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.cliente = self.cliente  # aseguramos que no cambie de cliente
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("clientes:detalle", kwargs={"pk": self.cliente.id})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cliente"] = self.cliente
        return context



class RutinaEliminarParaClienteView(DeleteView):
    model = Rutina
    template_name = "rutinas/confirmar_eliminar.html"

    def dispatch(self, request, *args, **kwargs):
        self.cliente = get_object_or_404(Cliente, pk=self.kwargs["cliente_id"])
        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return reverse_lazy("clientes:detalle", kwargs={"pk": self.cliente.id})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cliente"] = self.cliente
        return context
