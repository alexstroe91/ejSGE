cadena = "ay mi madre el Vini"

lista = [(i.upper(), i.lower()) for i in cadena]

#print(lista)

lista2 = ['i' if i in "aeiou" else i for i in cadena]

print(lista2)