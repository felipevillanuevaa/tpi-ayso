# promedio.py
# Programa para calcular el promedio de notas de un alumno
# Trabajo Integrador - Arquitectura y Sistemas Operativos

def calcular_promedio():
    notas = []
    print("=== Calculadora de Promedios ===")
    print("Ingrese 3 notas del alumno:\n")

    for i in range(3):
        while True:
            try:
                nota = float(input(f"Nota {i + 1}: "))
                if 0 <= nota <= 10:
                    notas.append(nota)
                    break
                else:
                    print("  La nota debe estar entre 0 y 10. Intente nuevamente.")
            except ValueError:
                print("  Valor inválido. Ingrese un número.")

    promedio = sum(notas) / len(notas)

    print("\n--- Resultado ---")
    print(f"Notas ingresadas: {notas}")
    print(f"Promedio: {promedio:.2f}")

    if promedio >= 6:
        print("Estado: APROBADO ✓")
    else:
        print("Estado: DESAPROBADO ✗")

if __name__ == "__main__":
    calcular_promedio()
