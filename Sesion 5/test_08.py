
"""
    Programación Orientada a Objetos en Python
    Participación
Requerimientos:
- Crea una clase alumno
- Debe tener un atributo de nacionalidad de valor peruano
- Crear un método que indicará el promedio del alumno
- Crear un método que indicará si el alumno está aprobado o no, de acuerdo a su promedio
- Tendrá tres notas, la nota inicial será de 0 para todos
- Obtener el nombre y distrito de residencia
"""

class Alumno:

    nota1 = 0
    def __init__(self, nombre, distrito, nota2, nota3, nacionalidad = "Peruano"):
        self.nombre = nombre
        self.distrito = distrito
        self.nota2 = nota2
        self.nota3 = nota3
        self.nacionalidad = nacionalidad

    def promedio(self):
        prom = (self.nota1 + self.nota2 + self.nota3) / 3
        self.prom = prom
        return prom

    def estado(self):
        if self.prom >= 10.5:
            return "Aprobado"
        else:
            return "Reprobado"

alumno1 = Alumno("Max", "El Agustino", 20, 18)

print("El promedio del alumno es: {}".format(alumno1.promedio()))
print("El estado del alumno es: {}".format(alumno1.estado()))
print("El nombre del alumno es: {}".format(alumno1.nombre))
print("El distrito del alumno es: {}".format(alumno1.distrito))