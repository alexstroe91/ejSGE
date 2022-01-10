import random
import math 

def mostrarLineas():
    numeroLineas = int(input("Introduce el numero de lineas que quieres mostrar: "))
    
    f = open("fichero.txt", "r")
    for i in range(numeroLineas):
        print(f.readline())

    f.close()  
        

listaNumeros = []

for i in range(1000):
    listaNumeros.append(random.randint(1,1000))
    
f = open("fichero.txt", "w")
    
for i in listaNumeros:
    
    cuadrado = i ** 2
    raiz = math.sqrt(i)
    cubo = i ** 3
    
    f.write("numero={}#cuadrado={}#raiz={}#cubo={}\n".format(i, round(cuadrado, 2), round(raiz,2), round(cubo,2)))

f.close()

mostrarLineas()