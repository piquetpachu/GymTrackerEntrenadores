from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from ejercicios.models import Ejercicio
from progreso.models import ProgresoEjercicio
from rutinas.models import Rutina

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
    rutinas = Rutina.objects.filter(cliente=cliente)

    return render(request, "rutinas/rutinas.html", {
        "rutinas": rutinas,
        "modo_cliente": True,  # se usa para personalizar el template
    })

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
        rir = request.POST.get("rir") or None
        rpe = request.POST.get("rpe") or None

        ProgresoEjercicio.objects.create(
            cliente=cliente,
            ejercicio=ejercicio,
            peso=peso or None,
            repeticiones=repeticiones or 0,
            notas=notas,
            rir=rir,
            rpe=rpe,
        )
        messages.success(request, "Progreso guardado correctamente.")
        return redirect("panel_cliente:dashboard")

    return render(request, "panel_cliente/registrar.html", {
        "cliente": cliente,
        "ejercicio": ejercicio,
    })

@login_required
def crear_rutina_cliente(request):
    if request.user.rol != "cliente":
        messages.error(request, "No tienes acceso a este panel.")
        return redirect("home")

    cliente = request.user.perfil_cliente
    ejercicios = Ejercicio.objects.all()

    if request.method == "POST":
        nombre = request.POST.get("nombre")
        descripcion = request.POST.get("descripcion", "")
        ejercicios_ids = request.POST.getlist("ejercicios")

        rutina = Rutina.objects.create(
            nombre=nombre,
            descripcion=descripcion,
            cliente=cliente
        )
        rutina.ejercicios.set(ejercicios_ids)
        rutina.save()

        messages.success(request, "Rutina creada exitosamente.")
        return redirect("panel_cliente:rutinas")

    return render(request, "panel_cliente/crear_rutina.html", {
        "cliente": cliente,
        "ejercicios": ejercicios
    })

@login_required
def detalle_rutina_cliente(request, rutina_id):
    if request.user.rol != "cliente":
        messages.error(request, "No tienes acceso a este panel.")
        return redirect("home")

    cliente = request.user.perfil_cliente
    rutina = get_object_or_404(Rutina, id=rutina_id, cliente=cliente)

    return render(request, "panel_cliente/detalle_rutina.html", {
        "rutina": rutina,
        "cliente": cliente,
        "ejercicios": rutina.ejercicios.all(),
    })

@login_required
def editar_rutina_cliente(request, rutina_id):
    if request.user.rol != "cliente":
        messages.error(request, "No tienes acceso a este panel.")
        return redirect("home")

    cliente = request.user.perfil_cliente
    rutina = get_object_or_404(Rutina, id=rutina_id, cliente=cliente)
    ejercicios = Ejercicio.objects.all().order_by("nombre")

    if request.method == "POST":
        rutina.nombre = request.POST.get("nombre")
        rutina.descripcion = request.POST.get("descripcion", "")
        ejercicios_ids = request.POST.getlist("ejercicios")
        rutina.ejercicios.set(ejercicios_ids)
        rutina.save()

        messages.success(request, "✏️ Rutina actualizada correctamente.")
        return redirect("panel_cliente:detalle_rutina", rutina_id=rutina.id)

    return render(request, "panel_cliente/editar_rutina.html", {
        "rutina": rutina,
        "ejercicios": ejercicios
    })


@login_required
def eliminar_rutina_cliente(request, rutina_id):
    if request.user.rol != "cliente":
        messages.error(request, "No tienes acceso a este panel.")
        return redirect("home")

    cliente = request.user.perfil_cliente
    rutina = get_object_or_404(Rutina, id=rutina_id, cliente=cliente)

    if request.method == "POST":
        rutina.delete()
        messages.success(request, "🗑️ Rutina eliminada correctamente.")
        return redirect("panel_cliente:rutinas")

    return render(request, "panel_cliente/eliminar_rutina.html", {"rutina": rutina})
