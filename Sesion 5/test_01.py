
"""Programación funcional con Python"""

def multiplicacion(a, b, c = 1000):
    #resultado = a * b * c
    #return resultado
    return a * b * c

print("El resultado de mi multiplicación es: {}".format(multiplicacion(40, 30)))

#Es correcto usar la función cambiando el valor del tercer miembro
print("El resultado de mi multiplicación es: {}".format(multiplicacion(40, 2, 100)))