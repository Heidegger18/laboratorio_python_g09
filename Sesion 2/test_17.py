"""Diccionarios en Python"""

"""del: eliminar un key y valor del diccionario"""

var_1 = {"nombre": "Margarita", "edad": 27, "promedio": 15}

"""
Para eliminar valores de nuestro diccionario
usamos a del delante de una variable
"""

del var_1["edad"]
del var_1["nombre"]

print("El diccionario actualizado es: {}".format(var_1))
