#tipos de datos


#conversion de muchas cosas a numero entero
a = int('123456')
print(a)

#truncar los decimales, quita todos los decimales despues del punto
b= int (12.1232465)
print(b)

#redondeo de numeros
c= round(12.456546, 3)
print(c)

#manejo expresion booleana

bool(None)
bool(0)
bool(0.0)
bool('')
bool(0.)

bool(True)
bool('a')
bool(1)

#convertir cosas a string

e= str(123465)
print(e, type(e))

f = list('abcdef')
print (f)

g = 'la casa es mia'.split(' ')
print(g)

i = 'la_casa_es_mia'.split('_')
print(i)

#dictionary
h = dict([(1,'a'),(2,'b'), (3,'l')])
print(h[3])

#arreglo distributivo
j = {'A': 'a', 'B': 'b'}
print(j['B'])

