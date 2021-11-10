
print("1 ----------------------------")

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