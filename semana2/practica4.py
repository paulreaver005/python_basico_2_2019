#crear un string con la palabra hola y el año 2019

anno = 2019
b = 'Hola '
a = str(anno)
concatenada = b + a

print(concatenada)

#crear el decimal 3.14 basado en el str 3 y el str 0.14

c = '3'
d = '0.14'

print(type(c), type(d))

sum = float(c) + float(d)
print(sum, type(sum))

#crear una lista de palabras usando la frase 'Hola_a_todos'

e = 'Hola_a_todos'.split('_')
print(e)

#crear un conjunto de letras usando la frase Bienvenido
f = set('Bienvenido')
print(f)