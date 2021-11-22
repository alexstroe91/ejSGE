palabra = input("Introduce una palabra: ")
palabraReves = ""

iNeg = -1
#[::-1]

for i in range(len(palabra)):
    palabraReves = palabraReves + str(palabra[i])
    iNeg -= 1
    
if (palabra).lower() == (palabraReves).lower():
    print("Es un palindromo")
else:
    print("No es un palindromo")