import csv


lista = []
pizzasTotales = []
dic = {}
ingredientes = ["carne", "bacon", "pollo", "peperoni", "atun"]

respuesta = 2

while respuesta ==2:
    ing1 = ""
    ing2 = ""
    ing3 = ""

    tamaño = int(input("Elige el tamaño de la pizza: 1 -  Mediana // 2 - Grande: "))

    if tamaño == 1:
        tamaño = "Mediana"
    elif tamaño == 2:
        tamaño = "Grande"

    #lista.append(tamaño)
    dic["Tamano"] = tamaño

    for i in range(len(ingredientes)):
        print(i + 1, " - ", ingredientes[i])
        
    ing1 = ingredientes[(int(input("Elige el ingrediente: ")) - 1)]
    ing2 = ingredientes[(int(input("Elige el ingrediente: ")) - 1)]
    ing3 = ingredientes[(int(input("Elige el ingrediente: ")) - 1)]
        
    #lista.append(ing1)
    #lista.append(ing2)
    #lista.append(ing3)
    
    dic["Ingrediente 1"] = ing1
    dic["Ingrediente 2"] = ing2
    dic["Ingrediente 3"] = ing3

    lista.append(dic)
    dic = {}
    
    respuesta = int(input("Quieres salir? [1-SI/2-NO]: "))

print(len(lista))
print(lista)

with open("pizzas.csv", "w") as fich:
    fieldnames = ['Tamano', 'Ingrediente 1', 'Ingrediente 2', 'Ingrediente 3']
    writer = csv.DictWriter(fich, fieldnames = fieldnames, extrasaction='ignore', delimiter = ';')
    writer.writeheader()
    for i in range(len(lista)):
        writer.writerow(lista[i])