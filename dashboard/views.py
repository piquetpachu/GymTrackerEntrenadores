from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from clientes.models import Cliente
from rutinas.models import Rutina
from progreso.models import ProgresoEjercicio
from django.utils.timezone import now

@login_required
def dashboard_entrenador(request):
    # 🔒 Solo muestra los clientes del entrenador logueado (si no es superuser)
    if request.user.is_superuser:
        clientes = Cliente.objects.all()
    else:
        clientes = Cliente.objects.filter(entrenadores=request.user)

    # Rutinas recientes
    rutinas_recientes = (
        Rutina.objects.filter(cliente__in=clientes)
        .select_related('cliente')
        .order_by('-id')[:5]
    )

    # Últimos progresos registrados
    progresos_recientes = (
        ProgresoEjercicio.objects.filter(cliente__in=clientes)
        .select_related('cliente', 'ejercicio')
        .order_by('-fecha')[:5]
    )

    context = {
        "clientes": clientes,
        "rutinas_recientes": rutinas_recientes,
        "progresos_recientes": progresos_recientes,
        "hoy": now(),
    }

    return render(request, "dashboard/entrenador.html", context)
