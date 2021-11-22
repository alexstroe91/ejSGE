import random
def listaaleatoria(tamano):
	#el _ significa no uso el valor
	lista=[]
	for _ in range(tamano):
		lista.append(random.randint(0,1000))
	return lista

lista = listaaleatoria(1000)

print(lista[:10])
    
print(lista[-10:])

print(lista[50:86])

print(lista[:100:2])