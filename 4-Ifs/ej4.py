import math

a = float(input("Valor 1: "))
b = float(input("Valor 2: "))
c = float(input("Valor 3: "))

#redondeo a 1 decimal para que haga la operacion y la igualdad bien
if round(math.pow(c, 2), 1) == round((math.pow(a, 2) + math.pow(b, 2)), 1):
    print("Es un triangulo rectángulo.")
elif (a == b and a != c) or (a == c and a != b) or (c == b and c != a):
    print("Es un triangulo isosceles.")
elif a == b and a == c:
    print("Es un triangulo equilatero.")
else:
    print("Es un triangulo escaleno.")
