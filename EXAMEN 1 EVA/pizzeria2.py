import os

totalDineroGanado = 0
totalPizzVegVendidas = 0
totalPizzaNOVegVendidas = 0

pizzMediana2 = 0
pizzMediana3 = 0
pizzMediana4 = 0
pizzGrande2 = 0
pizzGrande3 = 0
pizzGrande4 = 0

continuar = 2

os.system("cls")

def menu():
    os.system("cls")  
    print("1.- Crear Pizza")
    print("2.- Dinero total Ganado")
    print("3.- Cuantas pizzas Vegetarianas o No Vegetarianas se han vendido")
    print("4.- Cuantas pizzas medianas de 2, 3 y 4 ingredientes se han vendido")
    print("5.- Cuantas pizzas grandes de 2, 3 y 4 ingredientes se han vendido")
    print("0.- SALIR")
    
    
while continuar != 1:
    menu()
    opcion = int(input("Introduce la opcion: "))
    #menu de creacion de la pizza
    if opcion == 1:
        os.system("cls")
        
        ingredientesVegetarianos = ["cebolla", "queso", "tomate", "pimiento", "aceitunas"]
        ingredientesNoVegetarianos = ["carne", "bacon", "pollo", "peperoni", "atun"]

        pizzaVeg = int(input("¿Qué tipo de pizza quieres? [1- Vegetariana / 2- NO Vegetariana]: "))

        if pizzaVeg == 1:
            tamaño = int(input("¿Que tamaño quieres? [1- Mediana 10€ / 2- Grande 16€]: "))
            
            totalPizzVegVendidas += 1
            
            if tamaño == 1:
                precio = 10
                print("El precio es de 10€, con 2 ingredientes, por cada ingrediente mas son 10% mas en el precio")
                
                cantIngredientes = int(input("Cuantos ingredientes quieres?: [2 / 3 / 4]: "))
                
                if cantIngredientes == 2:
                    pizzMediana2 += 1
                elif cantIngredientes == 3:
                    pizzMediana3 += 1
                elif cantIngredientes == 4:
                    pizzMediana4 += 1
                
                ingSeleccionados = []
                for i in range(0, cantIngredientes):
                    
                    for ingrediente in ingredientesVegetarianos:   
                            
                        os.system("cls")
                        print("\n")
                        indice = 1
                        for i in ingredientesVegetarianos:
                            print(indice, "- ", i)
                            indice += 1
                        
                        print("")
                        
                    ingredienteElegido = int(input("Selecciona el ingrediente: "))
                    ingSeleccionados.append(ingredientesVegetarianos[ingredienteElegido-1])
                    
            elif tamaño == 2:
                precio = 16
                print("El precio es de 16€, con 2 ingredientes, por cada ingrediente mas son 15% mas en el precio")
                cantIngredientes = int(input("Cuantos ingredientes quieres?: [2 / 3 / 4]: "))
                
                if cantIngredientes == 2:
                    pizzGrande2 += 1
                elif cantIngredientes == 3:
                    pizzGrande3 += 1
                elif cantIngredientes == 4:
                    pizzGrande4 += 1
                
                ingSeleccionados = []
                for i in range(0, cantIngredientes):
                    
                    for ingrediente in ingredientesVegetarianos:   
                            
                        os.system("cls")
                        print("\n")
                        indice = 1
                        for i in ingredientesVegetarianos:
                            print(indice, "- ", i)
                            indice += 1
                        
                        print("")
                        
                    ingredienteElegido = int(input("Selecciona el ingrediente: "))
                    ingSeleccionados.append(ingredientesVegetarianos[ingredienteElegido-1])
            
        elif pizzaVeg == 2:
            tamaño = int(input("¿Que tamaño quieres? [1- Mediana 10€ / 2- Grande 16€]: "))
            
            totalPizzaNOVegVendidas += 1
            
            if tamaño == 1:
                precio = 10
                print("El precio es de 10€, con 2 ingredientes, por cada ingrediente mas son 10% mas en el precio")
                
                cantIngredientes = int(input("Cuantos ingredientes quieres?: [2 / 3 / 4]: "))
                
                if cantIngredientes == 2:
                    pizzMediana2 += 1
                elif cantIngredientes == 3:
                    pizzMediana3 += 1
                elif cantIngredientes == 4:
                    pizzMediana4 += 1
                
                ingSeleccionados = []
                for i in range(0, cantIngredientes):
                    
                    for ingrediente in ingredientesVegetarianos:   
                            
                        os.system("cls")
                        print("\n")
                        indice = 1
                        for i in ingredientesVegetarianos:
                            print(indice, "- ", i)
                            indice += 1
                        
                        for i in ingredientesNoVegetarianos:
                            print(indice, "- ", i)
                            indice += 1
                        print("")
                        
                    ingredienteElegido = int(input("Selecciona el ingrediente: "))
                    if ingredienteElegido <= 5:
                        ingSeleccionados.append(ingredientesVegetarianos[ingredienteElegido-1])
                    elif ingredienteElegido > 5:
                        ingSeleccionados.append(ingredientesNoVegetarianos[ingredienteElegido - 6])
                    
            elif tamaño == 2:
                precio = 16
                print("El precio es de 16€, con 2 ingredientes, por cada ingrediente mas son 15% mas en el precio")
                cantIngredientes = int(input("Cuantos ingredientes quieres?: [2 / 3 / 4]: "))
                            
                if cantIngredientes == 2:
                    pizzGrande2 += 1
                elif cantIngredientes == 3:
                    pizzGrande3 += 1
                elif cantIngredientes == 4:
                    pizzGrande4 += 1
                
                ingSeleccionados = []
                for i in range(0, cantIngredientes):
                    
                    for ingrediente in ingredientesVegetarianos:   
                            
                        os.system("cls")
                        print("\n")
                        indice = 1
                        for i in ingredientesVegetarianos:
                            print(indice, "- ", i)
                            indice += 1
                        
                        for i in ingredientesNoVegetarianos:
                            print(indice, "- ", i)
                            indice += 1
                        print("")
                        
                    ingredienteElegido = int(input("Selecciona el ingrediente: "))
                    if ingredienteElegido <= 5:
                        ingSeleccionados.append(ingredientesVegetarianos[ingredienteElegido-1])
                    elif ingredienteElegido > 5:
                        ingSeleccionados.append(ingredientesNoVegetarianos[ingredienteElegido - 6])
            

        print("Los ingredientes elegidos son:")
        print(ingSeleccionados)
        if tamaño == 1:
            if cantIngredientes == 3:
                precioFinal = precio + (precio*0.1)
            elif cantIngredientes == 4:
                precioFinal = precio + 2*(precio*0.1)
            else:
                precioFinal = precio
        elif tamaño == 2:
            if cantIngredientes == 3:
                precioFinal = precio + (precio*0.15)
            elif cantIngredientes == 4:
                precioFinal = precio + 2*(precio*0.15)
            else:
                precioFinal = precio
        
            
        print("El precio de la pizza es: ", precioFinal, "€")
        totalDineroGanado += precioFinal
            
        input("Pulsa ENTER para continuar")
        
    if opcion == 2:
        os.system("cls")  
        print("El dinero total ganado es de: ", totalDineroGanado, "€")
        input("Pulsa ENTER para continuar")
    
    if opcion == 3:
        os.system("cls")  
        print("Total pizzas Vegetarianas vendidas: ", totalPizzVegVendidas)
        print("Total pizzas NO Vegetarianas vendidas: ", totalPizzaNOVegVendidas)
        input("Pulsa ENTER para continuar")
    
    if opcion == 4:
        os.system("cls")  
        print("Pizzas medianas: ")
        print("Total pizzas medianas de 2 ingredientes vendidas: ", pizzMediana2)
        print("Total pizzas medianas de 3 ingredientes vendidas: ", pizzMediana3)
        print("Total pizzas medianas de 4 ingredientes vendidas: ", pizzMediana4)
        input("Pulsa ENTER para continuar")
    
    if opcion == 5:
        os.system("cls")  
        print("Pizzas grandes: ")
        print("Total pizzas grandes de 2 ingredientes vendidas: ", pizzGrande2)
        print("Total pizzas grandes de 3 ingredientes vendidas: ", pizzGrande3)
        print("Total pizzas grandes de 4 ingredientes vendidas: ", pizzGrande4)
        input("Pulsa ENTER para continuar")
    
    if opcion == 0:
        continuar = int(input("Quieres salir? [1-SI / 2-NO]: "))    
        