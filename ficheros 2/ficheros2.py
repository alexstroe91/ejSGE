import math

def mostrarLineas(numeroLineas):
       
    f = open("fichero.txt", "r")
    for i in range(numeroLineas):
        print(f.readline())

    f.close()

def contarlineas():
    f = open("fichero.txt", "r")
    cont = 0
    for i in f:
        cont += 1
    
    f.close()
    return cont
    

print("1.- Mostrar cabecera")
print("2.- Mostrar pie")
print("3.- Añadir")
print("4.- Borrar")
opcion = int(input("Elige una opcion: "))

if opcion == 1:
    lineas = int(input("Cuantas lineas quieres leer: "))
    mostrarLineas(lineas)
    
elif opcion == 2:
    lineas = int(input("Cuantas lineas quieres leer: "))
    
    lineasALeer = contarlineas() - lineas + 1
    
    contador = 1
    texto = " "
    
    f = open("fichero.txt", "r")
    
    for i in range(contarlineas()):
        while texto != "":
            
            texto = f.readline()
            if contador >= lineasALeer:
                print(texto)
            contador += 1
            
    
elif opcion == 3:
    
    f = open ("fichero.txt", "a")
    
    for i in range(10):
        
        numero = int(input("Introduce el numero: " + str(i+1) + ": "))
        cuadrado = numero ** 2
        raiz = math.sqrt(numero)
        cubo = numero ** 3
        
        f.write("numero={}#cuadrado={}#raiz={}#cubo={}\n".format(numero, round(cuadrado, 2), round(raiz,2), round(cubo,2)))
        
    f.close()
    

        
    