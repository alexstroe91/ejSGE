import random
import os

listaNum=[]

while len(listaNum)<100:
     listaNum.append(random.randint(0,100000))

nom=input("Dime el nombre de la carpeta a crear: ")
os.mkdir(os.path.join(os.getcwd(),nom))

for i in listaNum:
    rutaNumero = os.path.join(nom,str(i))
    os.mkdir(rutaNumero)

    nombreFichero = os.path.join(rutaNumero, (str(i) + ".txt"))
    f = open(nombreFichero, "w")

    f.write("numero=%d#cuadrada=%d#raiz=%.2fcubo=%d\n"%( i,(i**2),(i**1/2),(i**3)))
    
    f.close()



