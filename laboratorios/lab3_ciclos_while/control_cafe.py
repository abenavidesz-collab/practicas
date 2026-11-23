# ==============================================================
# Laboratorio guiado 1 - Ciclos while con bandera y contador
# Archivo: control_cafe.py
# Control de calidad en la tostadora "Café del Valle"
# ==============================================================

# ---------- Paso 0: constantes del problema ----------
CODIGO_SUPERVISOR = "CAFE2026"
MAX_INTENTOS = 3
PESO_OBJETIVO = 500     # gramos
TOLERANCIA = 10         # gramos
MAX_CONSECUTIVAS = 3    # defectuosas seguidas que detienen la línea

# ---------- Paso 1: acceso del supervisor (contador + bandera) ----------
intentos = 0
acceso_concedido = False

while intentos < MAX_INTENTOS and not acceso_concedido:
    codigo = input("Código de supervisor: ")
    intentos += 1
    if codigo == CODIGO_SUPERVISOR:
        acceso_concedido = True
    else:
        restantes = MAX_INTENTOS - intentos
        print(f"Código incorrecto. Intentos restantes: {restantes}")

if not acceso_concedido:
    print("Acceso bloqueado. Avise al jefe de planta.")
else:
    print("Acceso concedido. Inicie el registro (0 para terminar).")

    # ---------- Pasos 2 a 5: registro de bolsas ----------
    total_bolsas = 0
    aceptadas = 0
    defectuosas = 0
    consecutivas = 0
    peso_acumulado = 0.0
    peso_minimo = 0.0
    peso_maximo = 0.0
    linea_detenida = False
    terminar = False

    while not terminar and not linea_detenida:
        peso = float(input(f"Peso de la bolsa {total_bolsas + 1} (g): "))

        # Paso 3: validación de entrada
        while peso < 0:
            print("El peso no puede ser negativo.")
            peso = float(input(f"Peso de la bolsa {total_bolsas + 1} (g): "))

        if peso == 0:
            terminar = True     # valor centinela: no se cuenta como bolsa
        else:
            total_bolsas += 1
            peso_acumulado += peso

            # Reto: mínimo y máximo sin listas ni min()/max()
            if total_bolsas == 1:
                peso_minimo = peso
                peso_maximo = peso
            elif peso < peso_minimo:
                peso_minimo = peso
            elif peso > peso_maximo:
                peso_maximo = peso

            # Paso 4: clasificación (diferencia absoluta a mano)
            diferencia = peso - PESO_OBJETIVO
            if diferencia < 0:
                diferencia = -diferencia

            if diferencia <= TOLERANCIA:
                aceptadas += 1
                consecutivas = 0
                print(" OK")
            else:
                defectuosas += 1
                consecutivas += 1
                print(f" DEFECTUOSA ({consecutivas} seguidas)")
                # Paso 5: bandera de alarma
                if consecutivas == MAX_CONSECUTIVAS:
                    linea_detenida = True

    # ---------- Paso 6: reporte del turno ----------
    print("\n===== REPORTE DEL TURNO =====")
    print(f"Bolsas revisadas: {total_bolsas}")
    print(f"Aceptadas: {aceptadas}")
    print(f"Defectuosas: {defectuosas}")
    if total_bolsas > 0:
        porcentaje = defectuosas / total_bolsas * 100
        promedio = peso_acumulado / total_bolsas
        print(f"% defectuosas: {porcentaje:.1f} %")
        print(f"Peso promedio: {promedio:.1f} g")
        print(f"Peso más bajo: {peso_minimo:.1f} g")
        print(f"Peso más alto: {peso_maximo:.1f} g")
    if linea_detenida:
        print("ALERTA: línea detenida por 3 bolsas defectuosas seguidas.")
        print("Revise la dosificadora.")
