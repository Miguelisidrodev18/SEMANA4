import math

def grados_a_radianes(grados):
    if grados <= 0:
        raise ValueError("Los grados deben ser mayores que cero.")
    return (grados * math.pi) / 180

def radianes_a_grados(radianes):
    if radianes <= 0:
        raise ValueError("Los radianes deben ser mayores que cero.")
    return (radianes * 180) / math.pi

# Función para ingresar un valor numérico mayor que cero
def ingresar_valor(mensaje):
    while True:
        valor = input(mensaje)
        if valor.replace(".", "", 1).isdigit():
            return float(valor)
        else:
            print("Por favor, ingrese un valor numérico válido.")

# Menú principal
def menu():
    print("-----------Menú----------------")
    print("1. Convertir grados a radianes")
    print("2. Convertir radianes a grados")
    print("3. Salir")

    opcion = input("Seleccione una opción: ")

    return opcion

# Función principal
def main():
    while True:
        opcion = menu()

        if opcion == '1':
            grados = ingresar_valor("Ingrese los grados a convertir: ")
            radianes = grados_a_radianes(grados)
            print(f"{grados} grados son {radianes} radianes.")
        elif opcion == '2':
            radianes = ingresar_valor("Ingrese los radianes a convertir: ")
            grados = radianes_a_grados(radianes)
            print(f"{radianes} radianes son {grados} grados.")
        elif opcion == '3':
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()
