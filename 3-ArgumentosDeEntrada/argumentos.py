import sys
import math

base = sys.argv[1]
altura = sys.argv[2]
resultado = int(sys.argv[1]) * int(sys.argv[2])

print("El perimetro de un cuadrado es Base x Altura: {0} X {1} = {2}".format(base, altura, resultado))

radio = int(sys.argv[3])
resultadoCirculo = 2 * radio * math.pi 

print("El area de un ciruclo es 2 * pi * Radio ({0}) = {1}".format(radio, resultadoCirculo))
