#crear una funcion que agrege contactos a una agenda de diccionarios

agenda = {
    'juan perez' : {'telefono': [63158888, 898989898], 'correo': 'jperez@gmail.com'},
    'carlos rojas' : {'telefono': 87001030, 'correo': 'crojass@gmail.com'},
    'ana marin' : {'telefono': 91000130, 'correo': 'amarin@gmail.com'}
}



def add_agenda(nombre, telefono, correo):
    agenda[nombre] = {'telefono':telefono, 'correo':correo}



add_agenda('felipe perez', 88967069, 'feliphiño@gmail.com')

pass