import csv

datos = []

datos.append(["Local", "Visitante", "Resultado", "Tarjetas Amarillas", "Tarjetas Rojas", "Espectadores"])
datos.append(["Fuenlabrada", "Almeria", "1-0", 3,  0, 30000])
datos.append(["Valladolid", "Eibar", "1-1", 0,  0, 30000])
datos.append(["Oviedo", "Cartagena", "0-0", 2,  1, 30000])
datos.append(["Girona", "Almeria", "0-3", 3,  0, 30000])
datos.append(["Burgos", "Cartagena", "0-0", 1,  0, 30000])
datos.append(["Amorrebieta", "Lugo", "3-3", 2,  0, 30000])
datos.append(["Zaragoza", "Lugo", "1-3", 2,  0, 30000])
datos.append(["Malaga", "Fuenlabrada", "3-3", 2,  1, 30000])
datos.append(["Ibiza", "Ponferradina", "2-2", 3,  0, 30000])
datos.append(["Tenerife", "Huesca", "1-2", 4,  1, 30000])
datos.append(["Leganes", "Mirandes", "1-1", 2,  0, 30000])

with open("liga.csv", "w") as fich:
    writer = csv.writer(fich, lineterminator = "\n")
    writer.writerows(datos)
    
with open("liga.csv") as fich:
    lineas = csv.reader(fich, delimiter = ",")
    for linea in lineas:
        print(linea)
    