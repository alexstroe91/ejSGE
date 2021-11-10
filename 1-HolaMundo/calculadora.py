print("Que operacion quieres hacer?")
print("1.- sumar")
print("2.- restar")
print("3.- multiplicar")
print("4.- dividir")

opcion = int(input('Opcion: '))

if opcion == 1:
    num1 = int(input("Introduce el primer numero: "))
    num2 = int(input("Introduce el segundo numero: "))
    resultado = num1 + num2
    print("El resultado de sumar  ", num1, " y ", num2, " es ", resultado)
elif opcion == 2:
    num1 = int(input("Introduce el primer numero: "))
    num2 = int(input("Introduce el segundo numero: "))
    resultado = num1 - num2
    print("El resultado de restar  ", num1, " y ", num2, " es ", resultado)
elif opcion == 3:
    num1 = int(input("Introduce el primer numero: "))
    num2 = int(input("Introduce el segundo numero: "))
    resultado = num1 * num2
    print("El resultado de multiplicar  ", num1, " y ", num2, " es ", resultado)
elif opcion == 4:
    num1 = int(input("Introduce el primer numero: "))
    num2 = int(input("Introduce el segundo numero: "))
    resultado = num1 / num2
    print("El resultado de dividir  ", num1, " y ", num2, " es ", resultado)
    


