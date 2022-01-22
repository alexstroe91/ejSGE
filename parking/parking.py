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
    horaEntrada = (input("Hora ENTRADA: "))    
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
            horaSalida = (input("Hora Salida: "))
            ticket[2] = "Fuera"
            splitHoraEntrada = ticket[1].split(":")
            splitHoraSalida = horaSalida.split(":")
            diferencia = int(splitHoraSalida[0]) - int(splitHoraEntrada[0])
            if splitHoraSalida[1] < splitHoraEntrada[1]:
                diferencia -= 1
                
            tarifa = 3.5 * diferencia
            ticket.append(tarifa)
            
    if encontrado == False:
        print("La matricula introducida no existe.")
            

opcion = 0

while opcion != 3:
    opcion = menu()

    if opcion == 1:
        crearTicket()
    elif opcion == 2:
        cerrarTicket()
    elif opcion == 3:
        print("                 -------- Has salido --------")
        
        
print(listaCoches)