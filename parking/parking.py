listaCoches = []
coche = []

def menu():
    print("1.- Crear ticket")
    
    opcion = int(input("Elige a opcion: "))
    
    return opcion
    
def crearTicket():
    matricula = input("Matricula: ")
    horaEntrada = input("Hora entrada: ")
    estado = "Dentro"
    coche.append(matricula)
    coche.append(horaEntrada)
    coche.append(estado)
    
    listaCoches.append(coche)

if menu() == 1:
    crearTicket()
    
    

print(coche)
print(listaCoches)