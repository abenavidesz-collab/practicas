# ==============================================================
# Laboratorio guiado 2 - Ciclos for sin colecciones
# Archivo: ahorro_cooperativa.py
# Simulador de ahorro programado, Cooperativa "Ahorro Andino"
# ==============================================================

# ---------- Constantes ----------
BONO_FIDELIDAD = 0.01           # 1 % del saldo cada 12 meses
AUMENTO_ANUAL_DEPOSITO = 0.05   # reto: el depósito sube 5 % cada año nuevo

# ---------- Paso 1: datos del socio ----------
deposito = float(input("Depósito mensual ($): "))
meses = int(input("Plazo (meses): "))
while meses <= 0:
    print("El plazo debe ser de al menos 1 mes.")
    meses = int(input("Plazo (meses): "))
tasa_anual = float(input("Tasa de interés anual (%): "))
meta = float(input("Meta de ahorro ($): "))

tasa_mensual = tasa_anual / 100 / 12

# ---------- Pasos 2 a 4: tabla mes a mes ----------
saldo = 0.0
total_depositado = 0.0
total_intereses = 0.0
total_bonos = 0.0
meta_alcanzada = False
mes_meta = 0

print()
print(f"{'Mes':>4} {'Depósito':>10} {'Interés':>9} {'Bono':>8} {'Saldo':>11}")
for mes in range(1, meses + 1):
    saldo += deposito
    total_depositado += deposito

    interes = saldo * tasa_mensual
    saldo += interes
    total_intereses += interes

    bono = 0.0
    if mes % 12 == 0:
        bono = saldo * BONO_FIDELIDAD
        saldo += bono
        total_bonos += bono

    print(f"{mes:>4} {deposito:>10.2f} {interes:>9.2f} {bono:>8.2f} {saldo:>11.2f}")

    # Bandera: guarda solo el PRIMER mes en que se alcanza la meta
    if not meta_alcanzada and saldo >= meta:
        meta_alcanzada = True
        mes_meta = mes

# ---------- Paso 5: resumen ----------
print()
print(f"Total depositado: ${total_depositado:,.2f}")
print(f"Intereses ganados: ${total_intereses:,.2f}")
print(f"Bonos recibidos: ${total_bonos:,.2f}")
print(f"Saldo final: ${saldo:,.2f}")
if meta_alcanzada:
    print(f"La meta de ${meta:,.2f} se alcanza en el mes {mes_meta}.")
else:
    print(f"La meta de ${meta:,.2f} no se alcanza; faltan ${meta - saldo:,.2f}.")

# ---------- Paso 6: comparar tasas (ciclos anidados) ----------
print()
print("Comparación de tasas para el mismo plan:")
for tasa in range(4, 13, 2):
    tm = tasa / 100 / 12
    s = 0.0
    for mes in range(1, meses + 1):
        s += deposito
        s += s * tm
        if mes % 12 == 0:
            s += s * BONO_FIDELIDAD
    print(f"  {tasa:>2} % anual -> saldo final ${s:,.2f}")

# ---------- Reto final: depósito creciente ----------
print()
print("Modo depósito creciente (+5 % cada año nuevo):")
print(f"{'Mes':>4} {'Depósito':>10} {'Interés':>9} {'Bono':>8} {'Saldo':>11}")
deposito_actual = deposito
saldo_creciente = 0.0
meta_creciente = False
mes_meta_creciente = 0
for mes in range(1, meses + 1):
    # Meses 13, 25, 37...: mes % 12 == 1, pero el mes 1 no cuenta
    if mes > 1 and mes % 12 == 1:
        deposito_actual = deposito_actual * (1 + AUMENTO_ANUAL_DEPOSITO)
    saldo_creciente += deposito_actual
    interes = saldo_creciente * tasa_mensual
    saldo_creciente += interes
    bono = 0.0
    if mes % 12 == 0:
        bono = saldo_creciente * BONO_FIDELIDAD
        saldo_creciente += bono
    print(f"{mes:>4} {deposito_actual:>10.2f} {interes:>9.2f} {bono:>8.2f} {saldo_creciente:>11.2f}")
    if not meta_creciente and saldo_creciente >= meta:
        meta_creciente = True
        mes_meta_creciente = mes

print(f"Saldo final con depósito creciente: ${saldo_creciente:,.2f}")
if meta_alcanzada and meta_creciente:
    diferencia_meses = mes_meta - mes_meta_creciente
    print(f"Con depósito creciente la meta se alcanza en el mes {mes_meta_creciente}, "
          f"{diferencia_meses} mes(es) antes que con depósito fijo.")
elif meta_creciente:
    print(f"Con depósito creciente la meta se alcanza en el mes {mes_meta_creciente}; "
          "con depósito fijo no se alcanza.")
else:
    print("La meta tampoco se alcanza con depósito creciente.")
