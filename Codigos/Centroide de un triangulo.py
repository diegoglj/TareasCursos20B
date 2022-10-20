# -*- coding: utf-8 -*-
import numpy as np 

class Triangulo:
    
    def __init__(self, vertice1, vertice2, vertice3):
        self.vertice1 = vertice1
        self.vertice2 = vertice2
        self.vertice3 = vertice3
    def centroide(self):
        centroide = (self.vertice1 + self.vertice2 + self.vertice3)  / 3
        
        return centroide
    
print("\n")
print("Bienvenido a la funcion que calcula el centroide de cualquier triangulo")
    
    
x1 = eval(input('Ingrese la coordeanada x del primer vertice: '))
y1 = eval(input('Ingrese la coordenada y del primer vertice: '))

x2 = eval(input('Ingrese la coordeanada x del segundo vertice: '))
y2 = eval(input('Ingrese la coordenada y del segundo vertice: '))

x3 = eval(input('Ingrese la coordeanada x del tercer vertice: '))
y3 = eval(input('Ingrese la coordenada y del tercer vertice: '))
    
vertice1 = np.array([x1,y1])
vertice2 = np.array([x2,y2])
vertice3 = np.array([x3,y3])

if __name__ == '__main__':
    triangulo = Triangulo(vertice1, vertice2, vertice3)
    Centroide = triangulo.centroide()
    print(f'El centroide del triangulo dado es el punto {Centroide}')
    