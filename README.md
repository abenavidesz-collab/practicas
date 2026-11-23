# Tarea 2 — Estructuras iterativas en Python

## Descripción
Cuatro programas de consola en Python que resuelven situaciones operativas mediante estructuras iterativas (`while`, `for`, `while True`), contadores, acumuladores, validaciones e interrupción anticipada con `break`. Incluye además los seis laboratorios guiados del curso.

## Objetivos
- Seleccionar entre `while` y `for` según exista una condición de continuación o una cantidad definida de repeticiones.
- Diseñar ciclos con inicialización, condición, actualización y salida correctas.
- Emplear contadores, acumuladores y condicionales para producir resultados verificables.
- Validar entradas, implementar menús repetitivos y controlar una interrupción anticipada.

## Funcionalidades
| Ejercicio | Archivo | Estructura principal |
|---|---|---|
| 1. Control de temperatura de una cámara | `ejercicios/ejercicio_1_temperatura.py` | `while` |
| 2. Registro semanal de consumo de agua | `ejercicios/ejercicio_2_consumo_agua.py` | `for` + `range()` |
| 3. Administración de un estacionamiento | `ejercicios/ejercicio_3_estacionamiento.py` | `while True` + `if/elif/else` |
| 4. Control de abastecimiento de una expedición | `ejercicios/ejercicio_4_expedicion.py` | `for` + `while` (validación) + `break` |

## Requisitos previos
- Python 3.10 o superior
- Visual Studio Code (recomendado)
- No se usan bibliotecas externas

## Instrucciones de ejecución
```bash
git clone <url-del-repositorio>
cd <carpeta-del-repositorio>
python ejercicios/ejercicio_1_temperatura.py
python ejercicios/ejercicio_2_consumo_agua.py
python ejercicios/ejercicio_3_estacionamiento.py
python ejercicios/ejercicio_4_expedicion.py
```
En Windows puede usarse `py` en lugar de `python`.

## Estructura del repositorio
```
├── ejercicios/          # Los cuatro programas de la tarea
├── laboratorios/        # Los seis laboratorios guiados (uno por carpeta)
│   ├── lab1_menu/
│   ├── lab2_condicional_multiple/
│   ├── lab3_ciclos_while/
│   ├── lab4_ciclos_for/
│   ├── lab5_menu_while_true/
│   └── lab6_colecciones/
├── docs/
│   ├── Documentacion_Tarea2_SOFT-01.pdf   # Tablas de variables, diagramas y casos de prueba
│   ├── diagramas/       # Diagramas de flujo (.png)
│   └── evidencias/      # Salidas de consola de cada caso de prueba
└── README.md
```

## Autor
Andrés Benavides Zeledón

## Información académica
- **Universidad:** Universidad CENFOTEC
- **Curso:** SOFT-01 Principios de Programación 1 — Sección SCP0
- **Periodo:** 2026-C3
- **Docente:** Álvaro Cordero Peña
- **Fecha:** 22 de noviembre de 2026

## Estado del proyecto
Finalizado — versión 1.0 entregada.
