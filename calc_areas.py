# Escribe una función que calcule el área de un triángulo, recibiendo la altura y la base como parámetros
# Y otra función que calcule el área de un círculo recibiendo el radio del mismo.

import math

def area_tri(altura, base):
    return ((altura*base)/2)

def area_circ(radio):
    return (math.pi*(radio**2))

print(f"Área de triangulo: {area_tri(4,6)}")
print(f"Área del círculo: {area_circ(4)}")