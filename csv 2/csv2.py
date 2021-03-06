import csv
from posixpath import split

partidos = []
resultados = []

with open("liga.csv") as fich:
    lineas = csv.reader(fich, delimiter = ",")
    partidos = list(lineas)
    
partidos.pop(0)
    
totalTarjetas = 0
totalEspectadores = 0
totalPartidos = 0
    
for partido in partidos:
    resultados.append(partido[2].split("-"))
    
    totalTarjetas += int(partido[3])
    totalTarjetas += int(partido[4])
    
    totalEspectadores += int(partido[5])
    
    totalPartidos += 1
    
mediaEspectadores = totalEspectadores / totalPartidos
    
victoriasLocal = 0
victoriasVisitante = 0
totalGoles = 0

for resultado in resultados:
    if resultado[0] > resultado[1]:
        victoriasLocal += 1
    elif resultado[0] < resultado[1]:
        victoriasVisitante += 1
    
    totalGoles += int(resultado[0])
    totalGoles += int(resultado[1])
    

print("Hay" ,(victoriasLocal) , "victorias para los locales")
print("Hay" , (victoriasVisitante), "victorias para los visitantes")

if victoriasLocal > victoriasVisitante:
    print("Han ganado mas los equipos locales")
elif victoriasLocal < victoriasVisitante:
    print("Han ganado mas los equipos visitantes")
else:
    print("Han ganado los mismos partidos")
    
print("Se han marcado un total de",totalGoles, "goles")

print("Se han sacado un total de", totalTarjetas, "tarjetas")

print("Los espectadores totales han sido", round(totalEspectadores, 2))

print("La media de los espectadores ha sido de", round(mediaEspectadores, 2))