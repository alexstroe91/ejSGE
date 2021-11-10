respuesta = "s"

while respuesta != "n":

    print("1-sumar")
    print("2-restar")
    print("3-multiplicar")
    print("4-dividir")
    opcion = int(input("Elige una opcion: "))

    num1 = int(input("Introduce el primer numero: "))
    num2 = int(input("Introduce el segundo numero: "))

    if opcion == 1:
        print("{0} + {1} = {2}".format(num1, num2, num1 + num2))
    elif opcion == 2:
        print("{0} - {1} = {2}".format(num1, num2, num1 - num2))
    elif opcion == 3:
        print("{0} * {1} = {2}".format(num1, num2, num1 * num2))
    elif opcion == 4:
        print("{0} / {1} = {2}".format(num1, num2, num1 / num2))

    respuesta = input("Quiere seguir? (s/n): ")

print("Fin de programa")
