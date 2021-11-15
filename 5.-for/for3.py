#Crea una lista aleatoria de n elementos
from itertools import count
import random as rm
#seed fija una semilla de esta forma siempre salen los mismo números.
rm.seed(2021)
#Creamos una lista del 0 al 99
lista=list(range(1000))

#De la lista creamos una lista mas pequeña de forma aleatoria
#Sample extrae un elemento al azar de objeto iterable,el segundo parametro es el numero de veces lo hacemos 
lista=rm.choices(lista,k=100)

menor = lista[0]
mayor = lista[0]
menosrepetido = 0
masrepetido = 0
acumulador = 0 
for i in range(len(lista)):
    
    if menor > lista[i]:
        menor = lista[i]
    
    if mayor < lista[i]:
        mayor = lista[i]

    acumulador += lista[i]

    for j in range(len(lista)):
        if lista.count(lista[i]) > lista.count(lista[j]):
            masrepetido = lista[i]
        
        if lista.count(lista[i]) < lista.count(lista[j]):
            menosrepetido = lista[i]

media = acumulador / len(lista)

print(menor)
print(mayor)
print(media)
print(menosrepetido)
print(masrepetido)
