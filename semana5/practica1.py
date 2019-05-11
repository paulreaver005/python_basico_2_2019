#crear una clase bebe
#definir 4 acciones
#simular un día normal
#modificar el bebe para que tenga nombre
#metodo para crecer que ingrese edad= 1)

class Bebe:

    def __init__(self, nombre):
        self.bebe_nombre = nombre
        self.edad = 0
    def repirar(self):
        print('breath in and breath out')
    def comer(self):
        print('yum yum yum')
    def llorar(self):
        print('Waaaaaaaaaaaaaaaaaaaaaaaaa')
    def dormir(self):
        print('zzzzz **out of service** zzzzzz')

    def crecer(self, edad=1):
        self.edad += edad
        print ('Mi edad es: ', self.edad)
pass

ignacio = Bebe('ignacio')

#simulacion de un día
ignacio.repirar()
ignacio.llorar()
ignacio.comer()
ignacio.llorar()
ignacio.llorar()
ignacio.dormir()
ignacio.repirar()
ignacio.crecer(10)
ignacio.crecer()

print('Bebé como te llamas?')
print('Me llamo: ', ignacio.bebe_nombre)


