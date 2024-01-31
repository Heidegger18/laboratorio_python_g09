
"""Usando las propiedades de cadenas o strings"""

"""Métodos de strings"""

cadena = "Conexión de base de datos con Python"

cadena_2 = cadena.replace(cadena[0:8], "pppppp")

print("Cadena con reemplzado tiene el siguiente valor actualizado: {}".format(cadena_2))

"""Eliminando espacios en blanco de mi cadena (después)"""
cadena_3 = "Conexión a base de datos con Python      "
cadena_4 = cadena_3.rstrip()

print(cadena_3)
print("Mi cadena actualizada sin espacio en blanco es la siguiente: {}".format(cadena_4))

cadena_5 = "          Conexión a Base de Datos con Python"
cadena_6 = cadena_5.lstrip()

print(cadena_5)
print("Mi cadena actualizada sin espacios en blancos es: {}".format(cadena_6))


