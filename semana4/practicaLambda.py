#crear una calculadora que sume reste multiplique divide potencie y raiz

suma = lambda x,y : x+y
resta = lambda x,y : x-y
multiple = lambda x,y : x*y
divide = lambda x,y : x/y
import math
potencia = lambda x,y: math.pow(x,y)
raiz = lambda x,y : math.pow(x, 1/y)


x= 3
y = 2

lista_funciones = (suma,resta,multiple,divide,potencia,raiz)

for mi_funcion in lista_funciones:
    print('resultado=' , mi_funcion(x,y))

#crear un diccionario de funciones

print('con diccionario')
calculadora = {
    'suma' : suma,
    'suma1': lambda x,y : x+y,
    'resta': resta,
    'divide': divide,
    'multiple': multiple,
    'potencia': potencia,
    'raiz': raiz
}

for f in calculadora.keys():
    print('resultado=', calculadora[f](x,y))

print('usando values')
for f in calculadora.values():
    print('resultado=', f(x,y))

