from datetime import datetime

listaCoches = []
coche = []

def menu():
    print("1.- Crear ticket")
    print("2.- Cerrar ticket")
    print("3.- Salir")
    
    opcion = int(input("Elige a opcion: "))
    
    return opcion
    
def crearTicket():
    coche = []
    matricula = input("Matricula: ")
    horaEntrada = input("Hora y minuto ENTRADA: ")
    estado = "Dentro"
    coche.append(matricula)
    coche.append(horaEntrada)
    coche.append(estado)
    
    listaCoches.append(coche)
    
def cerrarTicket():
    buscarMatricula = input("Matricula a cerrar: ")
    encontrado = False
    
    for ticket in listaCoches:
        if ticket[0] == buscarMatricula:
            encontrado = True
            horaSalida = input("Hora y minuto SALIDA: ")
            
            
    

opcion = 0

while opcion != 3:
    opcion = menu()

    if opcion == 1:
        crearTicket()
    elif opcion == 2:
        print("")
    elif opcion == 3:
        print("                 -------- Has salido --------")
        
        

print(coche)
print(listaCoches)