from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Rutina, EntradaEjercicio
from .forms import RutinaForm, EntradaEjercicioForm

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

# CRUD de EntradaEjercicio
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
        return reverse_lazy("rutinas:detalle", kwargs={"rutina_id": self.kwargs["rutina_id"]})

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
