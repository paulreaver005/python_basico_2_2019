#t = tuple(['mango','uvas','pera','manzana'])

#1 declarar una tupla
t = ('mango','uvas','pera','manzana')

#2 agregar piña a la tupla
t1 = ('piña',)
t3 = tuple (['piña'])
t2 = t + t3
print(t2)

#
print(t2[::2])
#en reversa
print(t2[::-2])