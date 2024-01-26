
lista_1 = []
lista_2 = []

lista_1.append("Max")
lista_1.append(23)
lista_1.append("Ingeniería de Sistemas")

lista_2.append("Elvis")
lista_2.append(22)
lista_2.append("Ciencias de la Computación")

suma_de_listas = lista_1 + lista_2

print("Inversa suma de listas: {}".format(suma_de_listas.reverse()))

lista_1.pop(1)
lista_2.pop(1)

print("Los valores de la lista_1 son: {}".format(lista_1))
print("Los valores de la lista_2 son: {}".format(lista_2))