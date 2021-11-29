import sys

if (len(sys.argv) < 3):
    print("Has introducido menos parametros.")
elif (len(sys.argv) > 3):
    print("Has introducido menos parametros que los necesarios")
else:
  
    cantAñosBisiestos = 0  
    listaAñosBisiestos = []
    
    
    if int(sys.argv[1]) < int(sys.argv[2]):
        añoInicial = int(sys.argv[1])
        añoFinal = int(sys.argv[2])
        
        añoActual = añoInicial
        cantAñosBisiestos = 0
        
        while añoActual <= añoFinal:
            if añoActual % 4 == 0 and añoActual % 100 != 0:
                cantAñosBisiestos += 1
                listaAñosBisiestos.append(añoActual)
            if añoActual % 400 == 0:
                cantAñosBisiestos +=1
                listaAñosBisiestos.append(añoActual)
                    
            añoActual += 1
    
    elif int(sys.argv[1]) > int(sys.argv[2]):
        añoInicial = int(sys.argv[1])
        añoFinal = int(sys.argv[2])
        
        añoActual = añoInicial
        cantAñosBisiestos = 0
        
        while añoActual >= añoFinal:
            if añoActual % 4 == 0 and añoActual % 100 != 0:
                cantAñosBisiestos += 1
                listaAñosBisiestos.append(añoActual)
            if añoActual % 400 == 0:
                cantAñosBisiestos +=1
                listaAñosBisiestos.append(añoActual)
                    
            añoActual -= 1
    
    elif int(sys.argv[1]) == int(sys.argv[2]):
        
        añoInicial = int(sys.argv[1])
        añoFinal = int(sys.argv[2])
        
        añoActual = añoInicial
        cantAñosBisiestos = 0
        
        while añoActual <= añoFinal:
            if añoActual % 4 == 0 and añoActual % 100 != 0:
                cantAñosBisiestos += 1
                listaAñosBisiestos.append(añoActual)
            if añoActual % 400 == 0:
                cantAñosBisiestos +=1
                listaAñosBisiestos.append(añoActual)
                    
            añoActual += 1
            
 
print("Hay un total de: ", cantAñosBisiestos, " años bisiestos")
print(listaAñosBisiestos)