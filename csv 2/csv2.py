import csv
from posixpath import split

partidos = []
resultados = []

with open("liga.csv") as fich:
    lineas = csv.reader(fich, delimiter = ",")
    partidos = list(lineas)
    
partidos.pop(0)
    
for partido in partidos:
    resultados.append(partido[2].split("-"))
    
victoriasLocal = 0
victoriasVisitante = 0

for resultado in resultados:
    if resultado[0] > resultado[1]:
        victoriasLocal += 1
    elif resultado[0] < resultado[1]:
        victoriasVisitante += 1

if victoriasLocal > victoriasVisitante:
    print("Han ganado mas los equipos locales")
elif victoriasLocal < victoriasVisitante:
    print("Han ganado mas los equipos visitantes")
else:
    print("Han ganado los mismos partidos")