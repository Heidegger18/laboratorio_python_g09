
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
        self.velocidad = self.velocidad + aceleracion

    def frena(self):
        velocidad = self.velocidad - self.aceleracion
        if velocidad < 0:
            velocidad = 0
        self.velocidad = velocidad

carro_1 = Carro("Negro", 50)
print("El color del primer carro es: {}".format(carro_1.color))
print("La aceleración de mi primer carro es: {}".format(carro_1.aceleracion))
print("La cantidad de ruedas que tiene mi primer carro es: {}".format(carro_1.ruedas))

carro_2 = Carro("Azul", 70)
print("El color del segundo carro es: {}".format(carro_2.color))
print("La aceleración de mi segundo carro es: {}".format(carro_2.aceleracion))
print("La cantidad de ruedas que tiene mi segundo carro es: {}".format(carro_2.ruedas))

