
"""
    Programación Orientada a Objetos en Python
    Herencia en Python
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

"""Aplicando Herencia"""
"""Creamos nuestra clase hija"""

class CarroVolador(Carro):

    ruedas = 6

    def __init__(self, color, aceleracion, estado_volando = False):
        super().__init__(color, aceleracion)
        self.estado_volando = estado_volando

    def vuela(self):
        self.estado_volando = True

    def aterriza(self):
        self.estado_volando = False

carro_1 = Carro("Rojo", 45)

carro_volador = CarroVolador("Blanco", 55)

print("El color de mi carro volador es: {}".format(carro_volador.color))
print("El estado inicial de mi carro volador es: {}".format(carro_volador.estado_volando))

carro_volador.vuela()

print("El estado inicial de mi carro volador es: {}".format(carro_volador.estado_volando))

#print("El estado del carro 1 es: {}".format(carro_1.vuela()))
"""Esto no puede suceder por qué la herencia es solo sobre la clase hija"""