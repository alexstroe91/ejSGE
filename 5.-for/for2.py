from typing import FrozenSet


letra = (input("Introduce una letra: "))

numLineas = int(input("Introduce un numero de lineas: "))

cadena = ""

for i in range(numLineas):
    for j in range(numLineas * 2):
        if j >= numLineas - i and j <= numLineas + i:
            cadena += letra
        else:
            cadena += " "
    print(cadena)
    cadena = ""

frase = str(input("Introduce la frase: "))
desplazamiento = int(input("Introduce el desplazamiento: "))
resultado = ""

for j in range(len(frase)):

    if (ord(frase[j]) + desplazamiento) > 122:
        resultado += (chr(ord(frase[j]) + desplazamiento - 26) )
    else:
        resultado += (chr(ord(frase[j]) + desplazamiento))
        

print(resultado)
