def FiltraNota(nota):
        if 18<=nota<=20:
            return 'La calificación AD excelente'
        elif 14<=nota<=18:
            return'La calificación A muy bien'
        elif 10 <= nota <= 14:
            return'La calificación B bien'
        elif 0<=nota<=10:
            return 'La calificación C reprobado'

def ControlError(verificaNota):
    if verificaNota<0 or verificaNota>20:
        raise ValueError("El número que ingresaste debe estar dentro del ragon de 0 a 20 ")


if __name__ == "__main__":

    while True:
        try:
            nota = int(input("Ingrese su nota:    "))
            ControlError(nota)
            break
        except ValueError as MalDato:
            print(MalDato)

    Calificacion = FiltraNota(nota)

    print(Calificacion)