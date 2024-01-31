
"""Uso del 'for'"""

ingenierias = ["Software", "Sistemas", "Industrial", "Química", "Mecánica"]

print("El tamaño de mi lista es: {}".format(len(ingenierias)))

i = 0
for nombre in ingenierias:
    print(nombre)
    i = i + 1
    print("Valor de i: {}".format(i))
