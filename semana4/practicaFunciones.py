#hacer una funcion que me imprima en consola que imprima en consola

def piramide(h):

    for i in range(0, h):
        for j in range (0,  i + 1):
            print("*" , end=' ')
        print("\r")
c = piramide(10)

print('resuelto por profesor')
#resuelto por el profesor
def mi_triangulo(h):
    for i in range(1, h+1):
        print('*' * i)

mi_triangulo(10)

