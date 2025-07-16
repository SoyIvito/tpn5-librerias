"""
1. Escriba una función redondear() que permita redondear un número decimal de acuerdo al criterio: 
Si la parte decimal es mayor a 0.5 (por ejemplo 3.5), devolver el entero siguiente (en este caso, 4), 
si no devolver el entero inmediatamente anterior.
"""

#La funcion se encuentra en el archivo FUNCIONES.py
from funciones import redondear

Aredondear = float(input("Ingrese el numero a redondear: "))
print(redondear(Aredondear))
