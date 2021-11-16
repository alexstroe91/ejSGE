def sumar(op1, op2):
    print("{0} + {1} = {2}".format(op1, op2, op1 + op2))

def restar(op1, op2):
    print("{0} - {1} = {2}".format(op1, op2, op1 - op2))

def multiplicar(op1, op2):
    print("{0} * {1} = {2}".format(op1, op2, op1 * op2))

def dividir(op1, op2):
    if op2 == 0:
        print("El dividendo no puede ser 0")
    else:
        print("{0} / {1} = {2}".format(op1, op2, op1 / op2))

def menu():
    print("1-sumar")
    print("2-restar")
    print("3-multiplicar")
    print("4-dividir")

respuesta = "s"

while respuesta != "n":

    menu()
    
    opcion = int(input("Elige una opcion: "))

    num1 = int(input("Introduce el primer numero: "))
    num2 = int(input("Introduce el segundo numero: "))

    if opcion == 1:
        sumar(num1,num2)
    elif opcion == 2:
        restar(num1, num2)
    elif opcion == 3:
        multiplicar(num1, num2)
    elif opcion == 4:
        dividir(num1, num2)

    respuesta = input("Quiere seguir? (s/n): ")

print("Fin de programa")
