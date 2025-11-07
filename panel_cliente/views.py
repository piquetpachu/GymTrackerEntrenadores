from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from ejercicios.models import Ejercicio
from progreso.models import ProgresoEjercicio

@login_required
def dashboard_cliente(request):
    if request.user.rol != "cliente":
        messages.error(request, "No tienes acceso a este panel.")
        return redirect("home")

    cliente = request.user.perfil_cliente
    progresos_recientes = ProgresoEjercicio.objects.filter(cliente=cliente).order_by("-fecha")[:5]

    return render(request, "panel_cliente/dashboard.html", {
        "cliente": cliente,
        "progresos_recientes": progresos_recientes,
    })

@login_required
def mis_rutinas(request):
    if request.user.rol != "cliente":
        messages.error(request, "No tienes acceso a este panel.")
        return redirect("home")

    cliente = request.user.perfil_cliente
    rutinas = cliente.rutinas.all()
  # suponiendo que la relación ya existe

    return render(request, "panel_cliente/rutinas.html", {"rutinas": rutinas, "cliente": cliente})


@login_required
def registrar_progreso_cliente(request, ejercicio_id):
    if request.user.rol != "cliente":
        messages.error(request, "No tienes acceso a este panel.")
        return redirect("home")

    cliente = request.user.perfil_cliente
    ejercicio = get_object_or_404(Ejercicio, id=ejercicio_id)

    if request.method == "POST":
        peso = request.POST.get("peso")
        repeticiones = request.POST.get("repeticiones")
        notas = request.POST.get("notas", "")

        ProgresoEjercicio.objects.create(
            cliente=cliente,
            ejercicio=ejercicio,
            peso=peso or None,
            repeticiones=repeticiones or 0,
            notas=notas,
        )
        messages.success(request, "Progreso registrado correctamente.")
        return redirect("panel_cliente:dashboard")

    return render(request, "panel_cliente/registrar.html", {
        "cliente": cliente,
        "ejercicio": ejercicio,
    })
