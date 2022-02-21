import psycopg2
conn=None

sql = (
    """
    insert into futbolistas values ('87654321A', 'David', 'De Gea', 'Portero', 'Manchester United')
    """,
    """
    insert into futbolistas values ('54354312L', 'Paul', 'Pogba', 'Centrocampista', 'Manchester United')
    """,
    """
    insert into futbolistas values ('65465434R', 'Raphael', 'Varane', 'Defensa', 'Manchester United')
    """,
    """
    insert into futbolistas values ('76556734M', 'Harry', 'Maguire', 'Defensa', 'Manchester United')    
    """
    )

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
    for i in sql:
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
    

