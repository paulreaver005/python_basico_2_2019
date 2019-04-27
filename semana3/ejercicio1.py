#paso1 crear las listas individuales de cada categoría
misverduras = ['tomates','papas','cebollas','ajos']
misfrutas = ['piña','naranja','sandía']
miscarnes = ['mortadela', 'pollo', 'costilla de cerdo']
milimpieza = ['jabon', 'cloro','shampoo']

#paso2 crear una lista unificada de compras
milistadecompras = [miscarnes, misfrutas, misverduras,milimpieza]

#paso 4 agregar 2 elementos individuales a las listas
misverduras.append('chile')
misfrutas.append('mango')

#paso3 cuantos articulos vas a comprar
'''''''''
cantidad = 0

for categoria in milistadecompras:
    cantidad += len(categoria)

print(cantidad)


milista = []

for categoria in milistadecompras:
    milista.extend(categoria)
print(len(milista))
'''


#5vaciar la lista de verduras
#misverduras.clear()
#del misverduras
#misverduras.remove()
misverduras = []

print(milistadecompras)







#pass

#codigo que me diga cuantos elementos voy a comprar de la lista de compras
#agregar a la lista de verduras el chile y la lista de frutas el mango
#investigar cual es el efecto en la lista general
#utilizando pasos 1,2,4

