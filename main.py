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
#Al momento de probrar este ejercicio, quitar los comentarios

"""
import random

a = int(2)
b = int(10)

while True:
    numero = random.randint(a, b)
    print(f"{numero}")
"""


"""
5. Bola mágica: La bola mágica (Magic 8 ball) es un popular juguete usado
para la adivinación o para buscar consejo. Su mecanismo es muy simple:
ante una pregunta del usuario, la bola responde con una de 8 posibles
respuestas:
- Es seguro que sí
- Las chances son buenas
- Puedes contar con ello
- Pregúntame de nuevo más tarde
- Concéntrate y pregunta de nuevo
- No veo con claridad, intenta de nuevo
- Mi respuesta es no
- Mis fuentes me dicen que no
Escriba una función en Python para simular la bola mágica.

"""

import random
bola_magica = ["Es seguro que si", "Las chances son buenas", "Puedes contar con ello", "Preguntame de nuevo mas tarde", "Concentrate y pregunta de nuevo", "No veo con claridad, intenta de nuevo", "Mi respuesta es no", "Mis fuentes me dicen que no"]
respuesta = random.choice(bola_magica)

print(f"La bola magica dice {respuesta}")

