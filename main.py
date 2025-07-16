"""
1. Escriba una función redondear() que permita redondear un número decimal de acuerdo al criterio: 
Si la parte decimal es mayor a 0.5 (por ejemplo 3.5), devolver el entero siguiente (en este caso, 4), 
si no devolver el entero inmediatamente anterior.
"""

#La funcion se encuentra en el archivo FUNCIONES.py
from funciones import redondear

Aredondear = float(input("Ingrese el numero a redondear: "))
print(redondear(Aredondear))


"""
2. Coloque el módulo del ejercicio anterior dentro de un paquete. (funciones.py)
En un módulo que esté fuera de ese paquete, 
cree una función de suma de decimales que redondee el resultado haciendo uso de la función
redondear() del paquete recién creado.
"""

from funciones import redondear
def suma_redondeo(a, b):
    resultado = a + b
    return redondear(resultado)

a = float(input("Ingrese el primer numero decimal: "))
b = float(input("Ingrese el segundo numero decimal: "))
print(suma_redondeo(a,b))


"""
3. Usando el módulo datetime, 
escribe un programa que muestre la fecha y hora actuales del sistema.
"""

from datetime import *
fecha = datetime.now()
print(f"La fecha y actual es {fecha}")


"""
4. Escriba un programa que 
devuelva un número par al azar entre 2 y 10 
(pista: para comprobar si se pueden generar todos los números, pruebe ejecutar el programa dentro de un ciclo infinito).
"""

import random

a = int(2)
b = int(10)

while True:
    numero = random.randint(a, b)
    print(f"{numero}")