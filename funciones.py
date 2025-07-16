#ACTIVIDAD 1
def redondear(numero):
    parte_entera = int(numero)
    parte_decimal = numero - parte_entera

    if parte_decimal >= 0.5:
        redondeado = parte_entera + 1
    else:
        redondeado = parte_entera

    return redondeado