#crear un codigo que calcule las soluciones de la ecuacion cuadrática de la forma
#ax2 + bx + c = 0

#importar la clase de matematica

import math

#math.sqrt() esta es la raíz cuadrada
#elevar al cuadrado **2
#elevar al cubo **3
#elevar a cualquier potencia **11

a = float(input('Ingrese el valor de a:'))
b = float(input('Ingrese el valor de b:'))
c = float(input('Ingrese el valor de c:'))

discriminante = b**2-4*a*c

if discriminante < 0:
    raiz =  math.sqrt(-discriminante) * complex(0,1)
else:
    raiz =  math.sqrt(discriminante)

x1= (-b + raiz) / (2*a)
x2= (-b - raiz) / (2*a)

print('el resultado de X1 es ',  x1, 'y el resultado de X2 es ', x2 )