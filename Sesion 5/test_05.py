
"""Programación Orientada a Objetos en Python"""

class Carro:
    """Atributos"""
    ruedas = 4

    """Constructor: Valores que tendrá por defecto una instancia de mi clase"""
    def __init__(self, color, aceleracion):
        self.color = color
        self.aceleracion = aceleracion
        self.velocidad = 0

    """Métodos: Funciones de la Clase"""
    def acelerar(self):
        self.velocidad = self.velocidad + self.aceleracion

    def frena(self):
        velocidad = self.velocidad - self.aceleracion
        if velocidad < 0:
            velocidad = 0
        self.velocidad = velocidad

carro_1 = Carro("Blanco", 60)
print("El color de mi primero carro es: {}".format(carro_1.color))

carro_2 = Carro("Rojo", 80)
carro_2.marchas = 30000
print("Las marchas de mi segundo carro es: {}".format(carro_2.marchas))

#IMPORTANTE
"""No es posible llamar un atributo propio del objeto como si fuera de la clase"""