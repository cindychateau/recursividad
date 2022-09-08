#RECURSIVIDAD: Una función que se llama a sí misma
#1.- Caso base
#2.- Cómo se avanza
#3.- Volver a llamar a la función



#Función que me imprima N cantidad de veces la palabra Hello, RECURSIVO
#cantidad = 4
#PRINT HELLO (1)
#hello(3)

#cantidad = 3
#PRINT HELLO (2)
#hello(2)

#cantidad = 2
#PRINT HELLO (3)
#hello(1)

#cantidad = 1
#PRINT HELLO (4)
#hello(0)

#cantidad = 0
#------
def hello(cantidad):
    if cantidad > 0:
        print("Hello")
        hello(cantidad-1)

#Función de Cuenta Regresiva. La cual recibe un número e imprime los números desde el que recibe hasta el 0.
#Ej: recibo 10, imprimo 10 9 8 7 6 5 4 3 2 1 0
#num = 6
#PRINT 6
#cuentaRegresiva(5)

#cuentaRegresiva(5)
#num = 5
#PRINT 5
#cuentaRegresiva(4)

#cuentaRegresiva(4)
#num = 4
#PRINT 4
#cuentaRegresiva(3)

#cuentaRegresiva(3)
#num = 3
#PRINT 3
#cuentaRegresiva(2)
def cuentaRegresiva(num):
    if num >= 0:
        print(num)
        cuentaRegresiva(num-1)


hello(4)

cuentaRegresiva(6)

#sigma(5)
#num = 5
#RETURN 5 + sigma(4) = 5 + 10 = 15

#sigma(4)
#num = 4
#RETURN 4 + sigma(3) = 4 + 6 = 10

#sigma(3)
#num = 3
#RETURN 3 + sigma(2) = 3 + 3 = 6

#sigma(2)
#num = 2
#RETURN 2 + sigma(1) = 2 + 1 = 3

#sigma(1)
#num = 1
#RETURN 1
def sigma(num):
    if num == 1:
        return 1
    
    return num + sigma(num-1)


print(sigma(5))

#RETO GRUPAL: Funcion factorial recursiva. 
#factorial(4)
#num = 4
#RETURN 4 * factorial(3) = 4 * 6 = 24

#factorial(3)
#num = 3
#RETURN 3 * factorial(2) = 3 * 2 = 6

#factorial(2)
#num = 2
#RETURN 2 * factorial(1) = 2 * 1 = 2

#factorial(1)
#num = 1
#RETURN 1
def factorial(num):
    if num == 1:
        return 1
    return num * factorial(num-1)

print(factorial(4))

#RETO GRUPAL: Función que reciba como parámetro un número positivo y que te regrese el número recibido de la serie de fibonacci
#fibonacci(10) = 34
#Serie: 0 1 1 2 3 5 8 13 21 34 55 89 .....
#fibonacci(5)
#num = 5
#RETURN fibonacci(4) + fibonacci(3) = 2 + 1 = 3

#fibonacci(4)
#num = 4
#RETURN fibonacci(3) + fibonacci(2) = 1 + 1 = 2

#fibonacci(3)
#num = 3
#RETURN fibonacci(2) + fibonacci(1) = 1 + 0 = 1

#fibonacci(2)
#num = 2
#RETURN 1

#fibonacci(1)
#num = 1
#RETURN 0
def fibonacci(num):
    if num == 1:
        return 0
    elif num == 2:
        return 1
    else:
        return fibonacci(num - 1) + fibonacci(num - 2)

print(fibonacci(5))