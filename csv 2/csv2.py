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
