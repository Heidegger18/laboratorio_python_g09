
"""
    POO en Python
    Encapsulamiento
"""

class A():
    def __init__(self):
        """Encapsulamiento débil"""
        self.inicial = 10
        self._contador = 0 #Definiendo mi atributo privado

    def incrementa(self):
        self._contador = self._contador + 1

    def cuenta(self):
        return self._contador


class B():
    """Encapsulamiento"""
    def __init__(self):
        self.inicial = True
        self.__contador = 0 #Definiendo a mi atributo privado

    def incrementa(self):
        self.__contador = self.__contador + 1

    def cuenta(self):
        return self.__contador

var_1 = A()
var_1._contador
var_1.inicial = 20

var_1.incrementa()
var_1.incrementa()

print(var_1.cuenta())
print("Valor inicial de A: {}".format(var_1.inicial))
print("Contador de A: {}".format(var_1._contador))

var_2 = B()
var_2.inicial = False

var_2.incrementa()
var_2.incrementa()
var_2.incrementa()
var_2.incrementa()

print("Cuenta de B: {}".format(var_2.cuenta()))
print("Valor inicial de B: {}".format(var_2.inicial))

"""No es posible invocar a una variable por qué el encapsulamiento es fuerte"""
print("Contador de B: {}".format(var_2.__contador))