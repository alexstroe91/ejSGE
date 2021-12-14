cadena = "un día que el viento soplaba con fuerza#mira como se mueve aquella banderola -dijo un monje#lo que se mueve es el viento -respondió otro monje#ni las banderolas ni el viento, lo que se mueve son vuestras mentes -dijo el maestro"

cadena1 = cadena.replace("#", "\n")

lista = (cadena1.split("\n"))

for frase in range(1, len(lista)):
    print("-",lista[frase].capitalize())