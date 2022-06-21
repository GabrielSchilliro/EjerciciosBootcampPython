# Escribe una función que pueda decirte si un número (número entero) es primo o no.

def num_primo():
    num = int(input("Ingrese un número para saber si es primo: "))

    if num % 2 == 0:
        print(f"El numero ingresado ({num}), es primo")
    else:
        print(f"El numero ingresado ({num}), no es primo")

num_primo()