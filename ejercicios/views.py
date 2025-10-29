from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Ejercicio
from .forms import EjercicioForm


class EjercicioListaView(ListView):
    model = Ejercicio
    template_name = "ejercicios/lista.html"
    context_object_name = "ejercicios"
    
    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')
        
        if query:
            # Busca en nombre, descripción, grupo muscular y variante
            queryset = queryset.filter(
                Q(nombre__icontains=query) |
                Q(descripcion__icontains=query) |
                Q(grupo_muscular__icontains=query) |
                Q(variante__icontains=query)
            )
        return queryset

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
