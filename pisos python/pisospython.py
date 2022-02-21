# -*- coding: utf-8 -*-

sqlinsert = []
sqlCreateTable = []
texto = ""

with open("pisos.sql", "r", encoding="utf-8") as fic:
    texto = fic.read()
    while texto != "":
        sqlinsert.append(texto)
        texto = fic.read()

with open("tabla-pisos.sql", "r", encoding="utf-8") as fic:
    texto = fic.read()
    while texto != "":
        sqlCreateTable.append(texto)
        texto = fic.read()
        
for i in sqlCreateTable:
    print(i)
    
    