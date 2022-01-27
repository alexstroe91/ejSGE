pizzasTotales = []
dic = {}
ingredientes = ["carne", "bacon", "pollo", "peperoni", "atun"]

respuesta = 2

while respuesta ==2:
    ing1 = ""
    ing2 = ""
    ing3 = ""
    lista = []

    tamaño = int(input("Elige el tamaño de la pizza: 1 -  Mediana // 2 - Grande: "))

    if tamaño == 1:
        tamaño = "Mediana"
    elif tamaño == 2:
        tamaño = "Grande"

    lista.append(tamaño)

    for i in range(len(ingredientes)):
        print(i + 1, " - ", ingredientes[i])
        
    ing1 = ingredientes[(int(input("Elige el ingrediente: ")) - 1)]
    ing2 = ingredientes[(int(input("Elige el ingrediente: ")) - 1)]
    ing3 = ingredientes[(int(input("Elige el ingrediente: ")) - 1)]
        
    lista.append(ing1)
    lista.append(ing2)
    lista.append(ing3)

    pizzasTotales.append(lista)
    
    
    respuesta = int(input("Quieres salir? [1-SI/2-NO]: "))

for i in range(len(pizzasTotales)):
    dic[i] = pizzasTotales[i]
    
print(pizzasTotales)
print(len(dic))