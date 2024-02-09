
"""Programación funcional con Python"""

"""
Requisitos:
 - Ingresar dos números por terminal
 - En una función obtener si el segundo número ingresado es múltiplo del primero o viceversa
 - Retornar quién fue múltiplo de quién.
"""

def multiplo(a, b):

    if a % b == 0:
        return b,"es múltiplo de", a
    elif b % a == 0:
        return a, "es múltiplo de", b
    else:
        return "No hay múltiplo"

numero_1 = int(input("Ingrese un número: "))
numero_2 = int(input("Ingrese un número: "))

print(multiplo(numero_1, numero_2))