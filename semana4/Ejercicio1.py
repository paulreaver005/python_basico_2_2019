#agenda de contactos
#problema para encontrar un contacto por que hay que abrir todos los contactos
'''''''''
mi_agenda = {
    ('Juan', 'Perez'):[83013040, 'jperez@gmail.com'],
    ('Carlos', 'Rojas'):[87001030, 'crRojas@gmail.com'],
    ('Ana', 'Marin'):[91000013, 'amarin@gmail.com'],
}


print(mi_agenda)
'''

#resuelto por el profesor

agenda = {
    'juan perez' : {'telefono': [63158888, 898989898], 'correo': 'jperez@gmail.com'},
    'carlos rojas' : {'telefono': 87001030, 'correo': 'crojass@gmail.com'},
    'ana marin' : {'telefono': 91000130, 'correo': 'amarin@gmail.com'}
}



#cuantas personas hay en la agenda

print (len(agenda))
pass
#Cuales son los nombres de los contactos

print(agenda.keys())

#utilizando 1 imprima las informaciones de cada contacto
#nombre: juan perez telefono: 494987987 correo: paspls@gmail.com


for a, b in agenda.items():
    print('Nombre: ' , a, ' Telefono: ', b['telefono'], ' Correo:', b['correo'])


#resuelto por el profesor
#usando keys()
for persona in agenda.keys():
    print('nombre: ', persona, 'telefono: ', agenda[persona]['telefono'], 'correo: ', agenda[persona]['correo'] )




#Suponga que juan perez ahora tiene 2 telefonos


#agregar a sofia
#opcion :1 crear un diccionario para sofía
sofia = {'telefono': 33333333, 'correo': 'sofia@gmail.com'}
agenda ['sofia castro'] = sofia

#opcion :2
agenda.update({'sofia alfaro':sofia})
pass


