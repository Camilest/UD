from circulo import Circulo
from cuadrado import Cuadrado
from triangulo import Triangulo
from punto import Punto

p1 = Punto(1,1)
p2 = Punto(2,6)

opcion = input("Con que figuradesea trabajar \n 1.Cuadrado \n 2.Circulo \n 3.Triangulo \n3")

if opcion == '1':
    figura = Cuadrado(p1, p2)
elif opcion == '2' :
    figura = Circulo(p1,p2)
else:
    figura = Triangulo(p1,p2)

# cuadrado = Cuadrado(Punto(1,1), Punto(1,3))
figura.calcular_area()
figura.mostrar_area()
figura.calcular_perimetro()
figura.mostrar_perimetro()

# circulo = Circulo(Punto(10,10), Punto(5,5))

# circulo.calcular_area()
# circulo.mostrar_area()
# circulo.mostrar_perimetro()