
"""Programación funcional con Python"""

"""
Requisitos:
 - Solicitar al usuario cuatro numeros por consola
 - Crear una función que devuelva cúal es el mayor número de los 4 ingresados por el usuario
 - Finalmente elevar al cubo este número
"""

def mayor(n1, n2, n3, n4):

    if n1 >= n2 and n1 >= n3 and n1 >= n4:
        return n1
    elif n2 >= n1 and n2 >=n3 and n2 >= n4:
        return n2
    elif n3 >= n1 and n3 >=n2 and n3 >= n4:
        return n3
    elif n4 >= n1 and n4 >=n2 and n4 >= n3:
        return n4

numero_1 = float(input("Ingrese un numero: "))
numero_2 = float(input("Ingrese un numero: "))
numero_3 = float(input("Ingrese un numero: "))
numero_4 = float(input("Ingrese un numero: "))

print("El número mayor elevado al cubo es: {}".format(mayor(numero_1, numero_2, numero_3,numero_4) ** 3))
