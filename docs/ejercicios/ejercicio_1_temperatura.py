# ==============================================================
# Archivo: ejercicio_1_temperatura.py
# Curso: SOFT-01 Principios de Programación 1 - SCP0 - 2026-C3
# Autor: Andrés Benavides Zeledón
# Fecha: 22/11/2026
# Versión: 1.0
# Descripción: Simula el calentamiento de una cámara experimental.
#              Aumenta la temperatura en un incremento fijo por ciclo
#              (ciclo while) hasta alcanzar o superar el objetivo y
#              reporta la temperatura de cada ciclo y el total de ciclos.
# ==============================================================

# ---------- Entrada ----------
temperatura_inicial = float(input("Ingrese la temperatura inicial (°C): "))
temperatura_objetivo = float(input("Ingrese la temperatura objetivo (°C): "))
incremento = float(input("Ingrese el incremento por ciclo (°C): "))

# ---------- Validación de la configuración ----------
if temperatura_objetivo <= temperatura_inicial:
    print("Error: La temperatura objetivo debe ser mayor que la inicial.")
elif incremento <= 0:
    print("Error: El incremento debe ser mayor que cero.")
else:
    # ---------- Inicialización ----------
    temperatura_actual = temperatura_inicial
    ciclos = 0

    print("== Inicio de la simulación de calentamiento ==")

    # ---------- Iteración: se repite mientras no se alcance el objetivo ----------
    while temperatura_actual < temperatura_objetivo:
        # Actualización de la variable de control (evita el ciclo infinito)
        temperatura_actual = temperatura_actual + incremento
        ciclos = ciclos + 1
        print("Ciclo", ciclos, "-> Temperatura:", temperatura_actual, "°C")

    # ---------- Salida ----------
    print("== Resultados de la simulación ==")
    print("Temperatura final alcanzada:", temperatura_actual, "°C")
    print("Total de ciclos ejecutados:", ciclos)
