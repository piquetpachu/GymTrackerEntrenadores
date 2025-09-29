from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Ejercicio
from .forms import EjercicioForm

class EjercicioListaView(ListView):
    model = Ejercicio
    template_name = "ejercicios/lista.html"
    context_object_name = "ejercicios"

class EjercicioDetalleView(DetailView):
    model = Ejercicio
    template_name = "ejercicios/detalle.html"
    context_object_name = "ejercicio"

class EjercicioCrearView(CreateView):
    model = Ejercicio
    form_class = EjercicioForm
    template_name = "ejercicios/formulario.html"
    success_url = reverse_lazy("ejercicios:lista")

class EjercicioEditarView(UpdateView):
    model = Ejercicio
    form_class = EjercicioForm
    template_name = "ejercicios/formulario.html"
    success_url = reverse_lazy("ejercicios:lista")

class EjercicioEliminarView(DeleteView):
    model = Ejercicio
    template_name = "ejercicios/confirmar_eliminar.html"
    success_url = reverse_lazy("ejercicios:lista")
