import os
os.system("cls")

ingredientesVegetarianos = ["cebolla", "queso", "tomate", "pimiento", "aceitunas"]
ingredientesNoVegetarianos = ["carne", "bacon", "pollo", "peperoni", "atun"]

pizzaVeg = int(input("¿Qué tipo de pizza quieres? [1- Vegetariana / 2- NO Vegetariana]: "))

if pizzaVeg == 1:
    tamaño = int(input("¿Que tamaño quieres? [1- Mediana 10€ / 2- Grande 16€]: "))
    
    if tamaño == 1:
        precio = 10
        print("El precio es de 10€, con 2 ingredientes, por cada ingrediente mas son 10% mas en el precio")
        
        cantIngredientes = int(input("Cuantos ingredientes quieres?: [2 / 3 / 4]: "))
        
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
    
    if tamaño == 1:
        precio = 10
        print("El precio es de 10€, con 2 ingredientes, por cada ingrediente mas son 10% mas en el precio")
        
        cantIngredientes = int(input("Cuantos ingredientes quieres?: [2 / 3 / 4]: "))
        
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
            
        
        