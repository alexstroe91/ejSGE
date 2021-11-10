numero1 = int(input("Introduce el primer numero: "))
numero2 = int(input("Introduce el segundo numero: "))

if numero2 == 0:
    print("No se puede divir por 0")
else:
    print("{0} x {1} = {2}".format(numero1, numero2, numero1*numero2))