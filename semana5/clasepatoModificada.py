class Duck:
    def __init__(self, nombre):
        self.duck_nombre = nombre

    def quack(self):
        print('Quaaack!')

    def walk(self):
        print('Walks like a duck.')

#nace el pato

donald = Duck('donald')

donald.walk()
donald.quack()
print('Cual es tu nombre? ', donald.duck_nombre )