from math import pi
from punto import Punto
from figura import Figura

class Circulo(Figura):

    def __init__(self, p1,p2):
        Figura.__init__(self, p1,p2)
        self.nombre = "circulo"

    def calcular_area(self):
        radio = self.punto_uno.calcular_distancia(self.punto_dos)
        self.area = pi * radio ** 2
    
    def calcular_perimetro(self):
        lado = self.punto_uno.calcular_distancia(self.punto_dos)
        self.perimetro = 2 * pi * lado