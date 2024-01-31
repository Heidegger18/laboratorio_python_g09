
"""Usando las propiedades de cadenas o strings"""

"""Métodos de strings"""

cadena = "Python para la presentación de fraudes"

cadena_sin_espacios = cadena.split()

print("Cadena separada por espacios en blancos dentro del string: {}".format(cadena_sin_espacios))

for palabra in cadena_sin_espacios:
    print(palabra)