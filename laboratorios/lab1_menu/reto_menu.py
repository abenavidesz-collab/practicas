# Laboratorio guiado 2 - Reto: conversor de temperatura con menú sin ciclos
# Archivo: reto_menu.py

print("=== CONVERSOR DE TEMPERATURA ===")
print("1. Celsius a Fahrenheit")
print("2. Fahrenheit a Celsius")
print("3. Salir")

opcion = input("Elige una opción: ")

match opcion:
    case "1":
        c = float(input("Grados Celsius: "))
        print("Equivale a", c * 9 / 5 + 32, "°F")
    case "2":
        f = float(input("Grados Fahrenheit: "))
        print("Equivale a", round((f - 32) * 5 / 9, 2), "°C")
    case "3":
        print("Programa finalizado")
    case _:
        print("Opción no válida")
