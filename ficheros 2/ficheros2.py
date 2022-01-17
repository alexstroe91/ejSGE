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
    
elif opcion == 3:
    
    f = open ("fichero.txt", "a")
    
    for i in range(10):
        
        numero = int(input("Introduce el numero: " + str(i+1) + ": "))
        cuadrado = i ** 2
        raiz = math.sqrt(i)
        cubo = i ** 3
        
        f.write("numero={}#cuadrado={}#raiz={}#cubo={}\n".format(i, round(cuadrado, 2), round(raiz,2), round(cubo,2)))
        
    f.close()
        
    