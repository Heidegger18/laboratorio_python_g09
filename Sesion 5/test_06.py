
"""
    Programación Orientada a Objetos en Python
    Clase y métodos
"""

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

carro_1 = Carro("Azul", 70)
print("La velocidad inicial de mi carro 1 es: {}".format(carro_1.velocidad))

carro_1.acelerar()
carro_1.acelerar()
carro_1.acelerar()
carro_1.acelerar()

print(carro_1.velocidad)

carro_1.frena()
carro_1.frena()
carro_1.frena()

print(carro_1.velocidad)
