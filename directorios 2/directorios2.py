import shutil
import os
from posixpath import split


diccionario = {}
datos = {}
listaLimpia = []
cuadrado=[]
raiz=[]
numero=[]

def leer(ruta):
    
    txt=os.path.join(ruta,ruta+".txt")
    text = " "
    
    with open(os.path.join("numeros", txt),"r") as f:
        while text != "":
            text=f.readline()
            
            separado=text.split("#")
            
            return separado

def borrar(ruta):
    shutil.rmtree(ruta)     
            

            

listaNumerosDirectorio = os.listdir("numeros")

for i in range(len(listaNumerosDirectorio)):
    
    listaLimpia.append(leer(listaNumerosDirectorio[i]))
    
    cuadrado.append(listaLimpia[i][1].split("="))
    numero.append(listaLimpia[i][0].split("="))
    raiz.append(listaLimpia[i][2].split("="))
    datos[cuadrado[0][0]]=cuadrado[0][1]
    datos[raiz[0][0]]=raiz[0][1]
    diccionario[numero[0][1]]=datos
    cuadrado=[]
    raiz=[]
    numero=[]
    datos={}
    
print(diccionario)
ruta=input(("Dime el directorio a borrar: "))
borrar(ruta)