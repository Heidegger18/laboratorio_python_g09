
"""Requisitos
- Dentro de una empresa se va a solicitar pedir nombre y apellido de un empleado
- Distrito de residencia
- Sueldo y calculo del bono final año, que serà el triple del sueldo
mensual menos el 10 porciento.
- Todos los datos van a ingresarse a una lista
- Por asignación múltiple de variables asignar los valores de esta lista a 3 nuevas variables
- Mostrar por la terminal el mensaje de ("nombre" "apellido" recibirá "bono" soles)
"""

var_nombre = input("Ingrese su nombre: ")
var_apellido = input("Ingrese su apellido: ")
var_distrito = input("Ingrese su distrito de residencia: ")
var_sueldo = int(input("Ingrese su sueldo: "))

var_bono = (3 * var_sueldo) - (0.1 * var_sueldo)

lista = []
lista.append(var_nombre)
lista.append(var_apellido)
lista.append(var_distrito)
lista.append(var_sueldo)
lista.append(var_bono)

nombre, apellido, bono = lista[0], lista[1], lista[-1]

print("{} {} recibirá {} soles.".format(nombre, apellido, bono))
