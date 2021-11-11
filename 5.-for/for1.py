import math


print("///////////////////////////////////          1           ////////////////////////////////////////////////")

print("cadena")

cadena = "cadena"

for letra in cadena:
    print("    ", letra)

print("----------------------------")

print("lista")

lista = [1, 2.5, 'prueba', [5,6], 4]

for elemento in lista:
    print("    ", elemento)

print("----------------------------")
print("diccionario")

diccionario = {'nombre' : 'Carlos', 'edad' : 22, 'cursos': ['Python','Django','JavaScript'] }

for key in diccionario:
    print ("    ", key, ": ", diccionario[key])



cadena = input("Introduce una cadena: ")
cadenaNueva = ""
for letra in range(len(cadena)):
    cadenaNueva += cadena[letra].upper()
print("    " + cadenaNueva)

print("/////////////////////////////////////////          3          ////////////////////////////////////////////////")

listaNumeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

for num in listaNumeros:
    if (num % 2) == 0:
        print(num**2)
    else:
        print(math.sqrt(num))
