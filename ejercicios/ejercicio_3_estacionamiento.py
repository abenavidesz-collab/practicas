# ==============================================================
# Archivo: ejercicio_3_estacionamiento.py
# Curso: SOFT-01 Principios de Programación 1 - SCP0 - 2026-C3
# Autor: Andrés Benavides Zeledón
# Fecha: 22/11/2026
# Versión: 1.0
# Descripción: Administra un estacionamiento de 20 espacios mediante
#              un menú repetitivo (while True). Registra ingresos,
#              salidas con cobro por hora, consulta ocupación y
#              recaudación, y muestra un resumen al salir.
# ==============================================================

# ---------- Constantes ----------
CAPACIDAD_MAXIMA = 20
TARIFA_POR_HORA = 800

# ---------- Inicialización de contadores y acumulador ----------
vehiculos_presentes = 0
salidas_registradas = 0
recaudacion_total = 0

# ---------- Menú repetitivo ----------
while True:
    print()
    print("=== ESTACIONAMIENTO ===")
    print("1. Registrar ingreso")
    print("2. Registrar salida")
    print("3. Consultar ocupación")
    print("4. Consultar recaudación")
    print("5. Salir")
    opcion = input("Seleccione una opción (1-5): ")

    # ---------- Selección múltiple ----------
    if opcion == "1":
        # Ingreso: solo si hay espacios disponibles
        if vehiculos_presentes < CAPACIDAD_MAXIMA:
            vehiculos_presentes = vehiculos_presentes + 1
            print("[ÉXITO] Ingreso registrado. Vehículos presentes:", vehiculos_presentes)
        else:
            print("[ERROR] Estacionamiento lleno.")

    elif opcion == "2":
        # Salida: solo si hay al menos un vehículo
        if vehiculos_presentes > 0:
            horas_cobrar = int(input("Ingrese las horas por cobrar: "))
            # Validación: repetir mientras las horas no sean mayores que cero
            while horas_cobrar <= 0:
                print("[ERROR] Las horas deben ser mayores que 0.")
                horas_cobrar = int(input("Ingrese las horas por cobrar: "))

            monto_pago = horas_cobrar * TARIFA_POR_HORA
            vehiculos_presentes = vehiculos_presentes - 1
            salidas_registradas = salidas_registradas + 1
            recaudacion_total = recaudacion_total + monto_pago
            print("[ÉXITO] Monto a pagar: ₡", monto_pago)
            print("Vehículos restantes:", vehiculos_presentes)
        else:
            print("[ERROR] No hay vehículos en el estacionamiento.")

    elif opcion == "3":
        espacios_libres = CAPACIDAD_MAXIMA - vehiculos_presentes
        print("Espacios ocupados:", vehiculos_presentes)
        print("Espacios libres:", espacios_libres)

    elif opcion == "4":
        print("Recaudación total: ₡", recaudacion_total)
        print("Vehículos que han salido:", salidas_registradas)

    elif opcion == "5":
        # Salida explícita del ciclo
        break

    else:
        print("[ERROR] Opción no válida. Intente nuevamente.")

# ---------- Salida: resumen final ----------
print()
print("=== RESUMEN FINAL ===")
print("Vehículos presentes:", vehiculos_presentes)
print("Salidas registradas:", salidas_registradas)
print("Recaudación total: ₡", recaudacion_total)
