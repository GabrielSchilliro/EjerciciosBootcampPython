# Escribe un programa capaz de mostrar todos los números impares desde un número de inicio y otro final.
# Por ejemplo: teniendo numero_inicial = 2 y numero_final = 8, el programa debe imprimir por consola: [3, 5, 7]

num_inicial = int(input('Elija un numero inicial'))
num_final = int(input('Elija un numero final'))
num_impares = []

while num_final <= num_inicial:
    num_final: int(input('El segundo número debe ser mayor que el primero, introduce otro:'))

for impar in range(num_inicial, num_final + 1):
    if(impar % 2 != 0):
        num_impares.append(impar)

print(f"Lista de los números impares entre {num_inicial} y {num_final}: {num_impares}")