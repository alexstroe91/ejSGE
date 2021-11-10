import math
import sys

if len(sys.argv) == 3:
    
    if sys.argv[2] == "raiz" or sys.argv[2] == "r" or sys.argv[2] == "RAIZ":
        print(math.sqrt(float(sys.argv[1])))
    elif sys.argv[2] == "cuadrado" or sys.argv[2] == "c" or sys.argv[2] == "CUADRADO":
        print(math.pow(float(sys.argv[1]), 2))
    else:
        print("Argumentos incorrectos")

elif len(sys.argv) == 4:
    
    if sys.argv[3] == "suma":
        print("{0} + {1} = {2}".format(float(sys.argv[1]), float(sys.argv[2]), ( float(sys.argv[1]) + float(sys.argv[2]) ) ))
    elif sys.argv[3] == "resta":
        print("{0} - {1} = {2}".format(float(sys.argv[1]), float(sys.argv[2]), ( float(sys.argv[1]) - float(sys.argv[2]) ) ))
    elif sys.argv[3] == "multiplicar":
        print("{0} * {1} = {2}".format(float(sys.argv[1]), float(sys.argv[2]), ( float(sys.argv[1]) * float(sys.argv[2]) ) ))
    elif sys.argv[3] == "dividir":
        if sys.argv[2] == 0:
            print("No se puede divir por 0")
        else:
            print("{0} 7 {1} = {2}".format(float(sys.argv[1]), float(sys.argv[2]), ( float(sys.argv[1]) / float(sys.argv[2]) ) ))
    else:
        print("Argumentos incorrectos")
            
else:
    print("Argumentos incorrectos. Este programa necesita 2 o 3 argumentos")