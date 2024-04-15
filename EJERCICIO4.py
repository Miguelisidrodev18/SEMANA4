import math
def calcular_raiz_cuadrada(numero):
    return math.sqrt(numero)
def main():
    while True:
        try:
            print("\n*** Calculadora de Raíz Cuadrada ***")
            print("1. Calcular raíz cuadrada")
            print("2. Salir")
            opcion = int(input("Seleccione una opción: "))

            if opcion == 1:
                while True:
                    numero_str = input("Ingrese un número para calcular su raíz cuadrada (solo positivos): ")
                    if numero_str.replace(".", "", 1).isdigit():  # Verifica si el string representa un número
                        numero = float(numero_str)
                        if numero >= 0:
                            resultado = calcular_raiz_cuadrada(numero)
                            print("La raíz cuadrada de", numero, "es:", resultado)
                            break
                        else:
                            print("Error: El número debe ser positivo.")
                    else:
                        print("Error: Ingrese un número válido.")
            elif opcion == 2:
                print("Saliendo del programa...")
                break
            else:
                print("Opción inválida. Por favor, seleccione nuevamente.")
        except ValueError:
            print("Error: Ingrese un número válido para la opción.")

if __name__ == "__main__":
    main()
