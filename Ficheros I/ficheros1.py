import random
import math 

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

f = open("fichero.txt", "r")
print(f.read())

f.close()    