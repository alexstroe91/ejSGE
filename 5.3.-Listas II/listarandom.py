import random
def listaaleatoria(tamano):
	#el _ significa no uso el valor
	lista=[]
	for _ in range(tamano):
		lista.append(random.randint(0,1000))
	return lista