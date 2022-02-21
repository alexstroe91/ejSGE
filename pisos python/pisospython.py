# -*- coding: utf-8 -*-

import psycopg2
conn=None

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
        
        
textoNuevo = sqlinsert[0]
textoNuevo = textoNuevo.replace("pisos", "pisosNuevos")

sqlinsert.clear()
sqlinsert.insert(0, textoNuevo)   
     
textoNuevo = ""

textoNuevo = sqlCreateTable[0]
textoNuevo = textoNuevo.replace("pisos", "pisosNuevos")

sqlCreateTable.clear()
sqlCreateTable.insert(0, textoNuevo)
        
        
try:
    #creamos conexión
    conn = psycopg2.connect(
        host="127.0.0.1",
        database="pruebadb",
        user="pruebas",
        password="prueba123")
    #creamos un cursor
    cur = conn.cursor()
    #ejecutamos la query
        
    for i in sqlinsert:
        cur.execute(i)
        
    #extraemos la primera linea
    #print(cur.fetchone())
    #cerramos el cursor
    conn.commit()
    cur.close()
except (Exception, psycopg2.DatabaseError) as error:
    print(error)
finally:
    if conn is not None:
        cur.close()
        conn.close()
        print('Database connection closed.')        
    