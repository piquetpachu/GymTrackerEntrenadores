from django.db.models import Sum, F, FloatField, ExpressionWrapper
from .models import ProgresoEjercicio

def resumen_sesion(cliente_id, fecha):
    return (
        ProgresoEjercicio.objects.filter(cliente_id=cliente_id, fecha=fecha)
        .aggregate(
            total_reps=Sum("repeticiones"),
            total_peso=Sum(
                ExpressionWrapper(F("repeticiones") * F("peso"), output_field=FloatField())
            )
        )
    )
