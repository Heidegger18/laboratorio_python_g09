
"""Uso del flujo condicional 'if'"""

var1 = int(input("Ingrese su primer dato númerico: "))
var2 = int(input("Ingrese su segundo dato númerico: "))

if var1 > var2:
    print("El valor de var1 es mayor al segundo valor ingresado")
elif var1 == var2:
    print("Los valores ingresados son iguales")
else:
    print("El valor de var1 no es mayor que la var2")