from django.db import models

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Ejercicio
from .forms import EjercicioForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


class EjercicioListaView(LoginRequiredMixin, ListView):
    model = Ejercicio
    template_name = "ejercicios/lista.html"
    context_object_name = "ejercicios"

    def get_queryset(self):
        user = self.request.user
        # 👇 muestra los ejercicios globales y los del usuario logueado
        return Ejercicio.objects.filter(models.Q(visibilidad='global') | models.Q(usuario=user))


class EjercicioDetalleView(LoginRequiredMixin, DetailView):
    model = Ejercicio
    template_name = "ejercicios/detalle.html"
    context_object_name = "ejercicio"

    def get_queryset(self):
        user = self.request.user
        return Ejercicio.objects.filter(models.Q(visibilidad='global') | models.Q(usuario=user))


class EjercicioCrearView(LoginRequiredMixin, CreateView):
    model = Ejercicio
    form_class = EjercicioForm
    template_name = "ejercicios/formulario.html"
    success_url = reverse_lazy("ejercicios:lista")

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        form.instance.visibilidad = 'privado'  # 👈 fuerza el valor por defecto
        return super().form_valid(form)

class EjercicioEditarView(LoginRequiredMixin, UpdateView):
    model = Ejercicio
    form_class = EjercicioForm
    template_name = "ejercicios/formulario.html"
    success_url = reverse_lazy("ejercicios:lista")

    def get_queryset(self):
        # 👇 el usuario solo puede editar sus propios ejercicios
        return Ejercicio.objects.filter(usuario=self.request.user)


class EjercicioEliminarView(LoginRequiredMixin, DeleteView):
    model = Ejercicio
    template_name = "ejercicios/confirmar_eliminar.html"
    success_url = reverse_lazy("ejercicios:lista")

    def get_queryset(self):
        # 👇 solo puede eliminar los suyos
        return Ejercicio.objects.filter(usuario=self.request.user)

def form_valid(self, form):
    form.instance.usuario = self.request.user
    if self.request.user.is_staff:
        # Si es admin, deja el valor del formulario
        pass
    else:
        # Si es usuario común, fuerza a privado
        form.instance.visibilidad = 'privado'
    return super().form_valid(form)
