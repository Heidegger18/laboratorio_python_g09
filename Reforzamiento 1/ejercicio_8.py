
"""
8.Usando la condicional if imprimir por pantalla
si una lista está vacía o no, probar con una lista
vacía y otra con una lista vacía.
 """

def verificar_lista(l):
    if len(l) == 0:
        return "Lista vacía"
    else:
        return "Lista no vacía"


lista_1 = [1,2,3,4,5,6,7,8,9,10]
lista_2 = []

print(verificar_lista(lista_1))
print(verificar_lista(lista_2))

