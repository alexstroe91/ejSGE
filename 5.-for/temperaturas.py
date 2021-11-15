#libreria para tratar datos
import pandas as pd
#creamos un dataset que es una estructura ne formato tabla
df=pd.read_csv("./5.-for/temperaturas2.csv",sep=",")
#print(df.head())

# convertimos el dataset lista de listas
lista=df.to_numpy().tolist()
#print(lista)

acumuladorMaxima = 0 
acumuladorMinima = 0 
for i in range(len(lista)):
    print("fecha: %s, temperatura max: %s, temperatura min: %s, temperatura media: %.2f"
    % (str(lista[i][0]), str(lista[i][1]), str(lista[i][2]), ( (lista[i][1] + lista[i][2]) / 2) ))
    
    acumuladorMaxima += lista[i][1]
    acumuladorMinima += lista[i][2]

resultado = f'''
Temperatura media maxima: {round(acumuladorMaxima / len(lista), 2)}
Temperatura media minima: {round(acumuladorMinima / len(lista), 2)}
'''

print(resultado)