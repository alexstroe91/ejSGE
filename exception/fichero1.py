
#definimos la funcion
def funcExcepcion(lista1, lista2):
    
    #comprobamos que lista es mayor y lanzamos la excepcion correspondiente
    if len(lista1) > len(lista2):
        raise Exception("La lista 1 es mayor que la lista 2.")
    elif len(lista1) < len(lista2):
        raise Exception("La lista 1 es mayor que la lista 2.")
    else:
        #si son iguales de tamaño comprobamos que el divisor no sea 0 y si no es, se hace que
        #la division
        for i in range(len(lista1)):
            if lista2[i] == 0:
                raise ZeroDivisionError("No se puede dividir por 0.")
            else:
                print("{0} / {1} = {2}".format(lista1[i], lista2[i], lista1[i]/lista2[i]))
        