#paso1 crear las listas individuales de cada categoría
misverduras = ['tomates','papas','cebollas','ajos']
print(id(misverduras))
misfrutas = ['piña','naranja','sandía']
miscarnes = ['mortadela', 'pollo', 'costilla de cerdo']
milimpieza = ['jabon', 'cloro','shampoo']

#paso2 crear una lista unificada de compras
milistadecompras = [misverduras,misfrutas, miscarnes,milimpieza]

#paso 4 agregar 2 elementos individuales a las listas
misverduras.append('chile')
misfrutas.append('mango')

#5vaciar la lista de verduras
misverduras.clear()
#del misverduras
#misverduras.remove()
misverduras = []

print(id(misverduras))
print(milistadecompras)