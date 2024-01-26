
"""Listas en Python"""

"""Listas del: Eliminar un valor indicando el índice del valor en la lista"""

paises = []
paises.append("Perú")
paises.append("Brasil")
paises.append("Cánada")
paises.append("España")
paises.append("Chile")

print("Los valores de mi lista de paises son: {}".format(paises))

del paises[2]

print("Mi lista actualizada tiene los siguientes valores: {}".format(paises))
