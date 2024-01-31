
"""Usando las propiedades de cadenas o strings"""

"""
- Ingresar tu nombre y apellido por consola (cada valor tiene que estar en una variable diferente)
- Concatenar ambos valores en una sola variable
- Obtener el tamaño de tu nombre completo
- Imprimir el resultado final en mayúsculas
- Indicar mediante condicionales si el tamaño del nombre es mayor o no al del apellido
"""

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
nombre_completo = nombre + " " + apellido

print("El tamaño de mi nombre completo es: {}".format(len(nombre_completo)))
print("Mi nombre completo es maýusculas es: {}".format(nombre_completo.upper()))

if len(nombre) > len(apellido):
    print("El tamaño de mi nombre es mayor al tamaño de mi apellido")
elif len(nombre) == len(apellido):
    print("El tamaño de mi nombre es igual al tamaño de mi apellido")
else:
    print("El tamaño de mi nombre no es mayor al tamaño de mi apellido")