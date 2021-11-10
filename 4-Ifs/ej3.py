numero1 = int(input("Introduce el primer numero: "))
numero2 = int(input("Introduce el segundo numero: "))
numero3 = int(input("Introduce el tercer numero: "))

if numero1 > numero2 and numero1 > numero3:
    if numero2 > numero3:
        print(str(numero1) + " " + str(numero2) +  " " + str(numero3))
    else:
        print(str(numero1) +  " " + str(numero3) +  " " + str(numero2))
elif numero2 > numero1 and numero2 > numero3:
    if numero1 > numero3:
        print(str(numero2) + " " + str(numero1) +  " " + str(numero3))
    else:
        print(str(numero2) +  " " + str(numero3) +  " " + str(numero1))
else:
    if numero1 > numero2:
        print(str(numero3) +  " " + str(numero1) +  " " + str(numero2))
    else:
        print(str(numero3) +  " " + str(numero2) +  " " + str(numero1))
