
"""Uso del flujo condicional 'if'"""

"""if ternario"""

"""
Requisitos:
    - Ingresar por teclado el sueldo de un empleado
    - Si el sueldo es mayor de 3000 imprimir "Su sueldo no tiene bonificación"
    - Caso contrario "Su sueldo tiene bonificación este año"
"""

sueldo = int(input("Digite su sueldo: "))

sueldo = "Su sueldo no tiene bonificación" if sueldo > 3000 else "Su sueldo tiene bonificación este año"

print(sueldo)
