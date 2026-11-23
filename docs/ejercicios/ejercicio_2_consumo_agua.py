# ==============================================================
# Archivo: ejercicio_2_consumo_agua.py
# Curso: SOFT-01 Principios de Programación 1 - SCP0 - 2026-C3
# Autor: Andrés Benavides Zeledón
# Fecha: 22/11/2026
# Versión: 1.0
# Descripción: Registra el consumo de agua de 7 días (ciclo for con
#              range) y muestra el total semanal, el promedio diario,
#              el mayor consumo y los días que superan 150 L.
# ==============================================================

# ---------- Constantes ----------
TOTAL_DIAS = 7
UMBRAL_CONSUMO = 150.0

# ---------- Inicialización de acumulador y contadores ----------
consumo_total = 0.0
dias_superan_umbral = 0
mayor_consumo = 0.0

# ---------- Iteración: cantidad conocida de días ----------
for dia in range(1, TOTAL_DIAS + 1):
    # Entrada con validación: no se aceptan consumos negativos
    consumo_dia = float(input("Ingrese el consumo del día " + str(dia) + " (L): "))
    while consumo_dia < 0:
        print("Error: El consumo no puede ser menor a 0")
        consumo_dia = float(input("Ingrese el consumo del día " + str(dia) + " (L): "))

    # Acumulador del consumo semanal
    consumo_total = consumo_total + consumo_dia

    # Determinación del máximo por comparación (sin max())
    if dia == 1:
        mayor_consumo = consumo_dia
    elif consumo_dia > mayor_consumo:
        mayor_consumo = consumo_dia

    # Contador de días estrictamente por encima del umbral
    if consumo_dia > UMBRAL_CONSUMO:
        dias_superan_umbral = dias_superan_umbral + 1

# ---------- Proceso ----------
promedio_diario = consumo_total / TOTAL_DIAS

# ---------- Salida ----------
print("== Resumen semanal de consumo de agua ==")
print("Consumo total semanal:", consumo_total, "L")
print("Promedio diario:", round(promedio_diario, 2), "L")
print("Mayor consumo registrado:", mayor_consumo, "L")
print("Días que superaron", UMBRAL_CONSUMO, "L:", dias_superan_umbral)
