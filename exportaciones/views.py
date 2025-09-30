import openpyxl
from openpyxl import Workbook
from openpyxl.styles import Font, Alignment, PatternFill, Border, Side
from openpyxl.utils import get_column_letter
from django.http import HttpResponse
from progreso.models import Progreso
from clientes.models import Cliente
from rutinas.models import Rutina, EntradaEjercicio


# Estilos comunes
bold_font = Font(bold=True, size=12, color="FFFFFF")
title_font = Font(bold=True, size=14)
header_fill = PatternFill("solid", fgColor="4F81BD")  # azul
center_align = Alignment(horizontal="center", vertical="center")
thin_border = Border(
    left=Side(style="thin"),
    right=Side(style="thin"),
    top=Side(style="thin"),
    bottom=Side(style="thin"),
)


def exportar_progreso_excel(request, cliente_id):
    cliente = Cliente.objects.get(pk=cliente_id)
    progresos = Progreso.objects.filter(cliente=cliente).order_by("fecha")

    wb = Workbook()
    ws = wb.active
    ws.title = "Progreso"

    # Título
    ws.merge_cells("A1:I1")
    ws["A1"] = f"Progreso de {cliente.nombre}"
    ws["A1"].font = title_font
    ws["A1"].alignment = center_align

    # Encabezados
    headers = ["Fecha", "Peso (kg)", "Altura (cm)", "IMC", "Cintura", "Pecho", "Brazo", "Pierna", "Notas"]
    ws.append(headers)

    for col in range(1, len(headers) + 1):
        cell = ws.cell(row=2, column=col)
        cell.font = bold_font
        cell.fill = header_fill
        cell.alignment = center_align
        cell.border = thin_border

    # Filas de datos
    for p in progresos:
        fila = [
            p.fecha.strftime("%d-%m-%Y"),
            p.peso_kg,
            p.altura_cm,
            round(p.peso_kg / ((p.altura_cm / 100) ** 2), 2) if p.altura_cm else "",
            p.cintura_cm,
            p.pecho_cm,
            p.brazo_cm,
            p.pierna_cm,
            p.notas,
        ]
        ws.append(fila)

        for col in range(1, len(fila) + 1):
            cell = ws.cell(row=ws.max_row, column=col)
            cell.alignment = center_align
            cell.border = thin_border

    # Ajustar ancho
        for i, col in enumerate(ws.columns, 1):  # arranca desde 1
            max_length = 0
            column = get_column_letter(i)
            for cell in col:
                if cell.value:
                    max_length = max(max_length, len(str(cell.value)))
            adjusted_width = (max_length + 2)
            ws.column_dimensions[column].width = adjusted_width

    # Exportar
    response = HttpResponse(
        content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )
    response["Content-Disposition"] = f'attachment; filename="Progreso_{cliente.nombre}.xlsx"'
    wb.save(response)
    return response


def exportar_rutina_excel(request, rutina_id):
    rutina = Rutina.objects.get(pk=rutina_id)
    entradas = EntradaEjercicio.objects.filter(rutina=rutina).select_related("ejercicio")

    wb = Workbook()
    ws = wb.active
    ws.title = rutina.nombre[:30]

    # Título
    ws.merge_cells("A1:E1")
    ws["A1"] = f"Rutina: {rutina.nombre}"
    ws["A1"].font = title_font
    ws["A1"].alignment = center_align

    ws.append([])  # fila en blanco

    # Encabezados
    headers = ["Ejercicio", "Series", "Repeticiones", "Descanso (segundos)", "Notas"]
    ws.append(headers)

    for col in range(1, len(headers) + 1):
        cell = ws.cell(row=3, column=col)
        cell.font = bold_font
        cell.fill = header_fill
        cell.alignment = center_align
        cell.border = thin_border

    # Filas con ejercicios
    for entrada in entradas:
        fila = [
            entrada.ejercicio.nombre,
            entrada.series,
            entrada.repeticiones,
            entrada.descanso_segundos,
            entrada.notas,
        ]
        ws.append(fila)

        for col in range(1, len(fila) + 1):
            cell = ws.cell(row=ws.max_row, column=col)
            cell.alignment = center_align
            cell.border = thin_border

    # Ajustar ancho
    ws.column_dimensions["A"].width = 30
    ws.column_dimensions["B"].width = 12
    ws.column_dimensions["C"].width = 15
    ws.column_dimensions["D"].width = 20
    ws.column_dimensions["E"].width = 25

    # Exportar
    response = HttpResponse(
        content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )
    response["Content-Disposition"] = f'attachment; filename="Rutina_{rutina.nombre}.xlsx"'
    wb.save(response)
    return response
