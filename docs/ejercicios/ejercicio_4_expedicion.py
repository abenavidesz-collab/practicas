# ==============================================================
# Archivo: ejercicio_4_expedicion.py
# Curso: SOFT-01 Principios de Programación 1 - SCP0 - 2026-C3
# Autor: Andrés Benavides Zeledón
# Fecha: 22/11/2026
# Versión: 1.0
# Descripción: Simula el consumo diario de agua y alimento de una
#              expedición. Recorre las jornadas con un ciclo for,
#              valida consumos con while e interrumpe con break si un
#              recurso se agota. Al final presenta un informe.
# ==============================================================

# ---------- Constantes ----------
AGUA_INICIAL = 150.0
ALIMENTO_INICIAL = 100.0
MIN_JORNADAS = 1
MAX_JORNADAS = 30

# ---------- Inicialización ----------
agua_disponible = AGUA_INICIAL
alimento_disponible = ALIMENTO_INICIAL
agua_consumida_total = 0.0
alimento_consumido_total = 0.0
dias_completados = 0
expedicion_interrumpida = False

print("Suministros iniciales -> Agua:", agua_disponible, "L | Alimento:", alimento_disponible, "unid.")

# ---------- Entrada validada: cantidad de jornadas ----------
jornadas_planeadas = int(input("Ingrese la cantidad de jornadas (1-30): "))
while jornadas_planeadas < MIN_JORNADAS or jornadas_planeadas > MAX_JORNADAS:
    print("[ERROR] La cantidad de jornadas debe ser un entero entre", MIN_JORNADAS, "y", MAX_JORNADAS)
    jornadas_planeadas = int(input("Ingrese la cantidad de jornadas (1-30): "))

# ---------- Iteración: recorrido de las jornadas planeadas ----------
for dia in range(1, jornadas_planeadas + 1):
    # Verificación al iniciar la jornada
    if agua_disponible <= 0 or alimento_disponible <= 0:
        expedicion_interrumpida = True
        break

    print()
    print("--- JORNADA", dia, "DE", jornadas_planeadas, "---")
    print("Disponible al iniciar -> Agua:", agua_disponible, "L | Alimento:", alimento_disponible, "unid.")

    # Validación del consumo de agua
    consumo_agua = float(input("Consumo de agua (L): "))
    while consumo_agua <= 0 or consumo_agua > agua_disponible:
        if consumo_agua <= 0:
            print("[ERROR] El consumo de agua debe ser una cantidad positiva mayor a 0.")
        else:
            print("[ERROR] El consumo excede el agua disponible:", agua_disponible, "L")
        consumo_agua = float(input("Consumo de agua (L): "))

    # Validación del consumo de alimento
    consumo_alimento = float(input("Consumo de alimento (unid.): "))
    while consumo_alimento <= 0 or consumo_alimento > alimento_disponible:
        if consumo_alimento <= 0:
            print("[ERROR] El consumo de alimento debe ser una cantidad positiva mayor a 0.")
        else:
            print("[ERROR] El consumo excede el alimento disponible:", alimento_disponible, "unid.")
        consumo_alimento = float(input("Consumo de alimento (unid.): "))

    # Actualización de existencias, acumuladores y contador
    agua_disponible = agua_disponible - consumo_agua
    alimento_disponible = alimento_disponible - consumo_alimento
    agua_consumida_total = agua_consumida_total + consumo_agua
    alimento_consumido_total = alimento_consumido_total + consumo_alimento
    dias_completados = dias_completados + 1

    print("[REGISTRO] Jornada", dia, "completada.")
    print("Saldo restante -> Agua:", agua_disponible, "L | Alimento:", alimento_disponible, "unid.")

    # Interrupción anticipada si un recurso se agotó y quedan jornadas
    if (agua_disponible == 0 or alimento_disponible == 0) and dia < jornadas_planeadas:
        print("[ALERTA CRÍTICA] Uno o más suministros se han agotado por completo.")
        print("No es posible continuar al día siguiente. Interrumpiendo expedición...")
        expedicion_interrumpida = True
        break

# ---------- Proceso: promedios sobre jornadas reales ----------
if dias_completados > 0:
    promedio_agua = agua_consumida_total / dias_completados
    promedio_alimento = alimento_consumido_total / dias_completados
else:
    promedio_agua = 0.0
    promedio_alimento = 0.0

if expedicion_interrumpida:
    estado_expedicion = "INTERRUMPIDA ANTICIPADAMENTE POR AGOTAMIENTO DE SUMINISTROS"
else:
    estado_expedicion = "COMPLETADA EXITOSAMENTE"

# ---------- Salida: informe final ----------
print()
print("===== INFORME FINAL DE LA EXPEDICIÓN =====")
print("Estado de la expedición:", estado_expedicion)
print("Días completados:", dias_completados, "de", jornadas_planeadas)
print("Agua total consumida:", agua_consumida_total, "L")
print("Alimento total consumido:", alimento_consumido_total, "unid.")
print("Agua restante:", agua_disponible, "L")
print("Alimento restante:", alimento_disponible, "unid.")
print("Promedio diario agua:", round(promedio_agua, 2), "L/día")
print("Promedio diario alimento:", round(promedio_alimento, 2), "unid./día")
