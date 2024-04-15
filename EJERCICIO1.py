def interes_simple(saldo, tasa, tiempo):

    interes = saldo * tasa * tiempo
    monto_total = saldo + interes
    return monto_total

#Definimos función de calcular el valor final.
def calculo():
    try:
        saldo = float(input("Ingrese el monto principal: "))
        tasa = float(input("Ingrese la tasa de interés (en decimal): "))
        tiempo = int(input("Ingrese el tiempo en años: "))

        if saldo < 0 or tasa < 0 or tiempo < 0:
            print("Error: los valores ingresados deben ser positivos.")
        else:
            monto_final = interes_simple(saldo, tasa, tiempo)
            print("El monto final después de", tiempo, "años es:", monto_final)
    except ValueError:
        print("Error: asegúrese de ingresar valores numéricos válidos.")

if __name__ == "__main__":
    calculo()
