# Escribe una función que pueda decirte si un año (número entero) es bisiesto o no.

def anio_bisiesto():
    anio = int(input("Introduce un año y veamos si es bisiesto "))

    if anio % 4 == 0:
        print(f"El año {anio} es bisiesto")
    else:
        print(f"el año {anio} no es bisiesto :(")

anio_bisiesto()