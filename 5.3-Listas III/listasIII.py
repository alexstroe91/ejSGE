import os

continuar = "s"
listaUsuarios = []
id = 1

#muestra las opciones del menu
def menu ():
    os.system("cls")
    print("0.- Salir")
    print("1.- Añadir usuario")
    print("2.- Mostrar todos los usuarios")
    print("3.- Modificar usuarios dado un ID")
    print("4.- Borrar usuario dado un ID")
    print("5.- Mostrar solo las fechas")
    
#pide los datos del usuario y lo añade a la lista
def añadirUser(id):
    diaFecha = int(input("Introduce el dia: "))
    mesFecha = int(input("Introduce el mes: "))
    añoFecha = int(input("Introduce el año: "))
        
    rol = input("Rol del usuario: [usuario, usuario avanzado, admin]: ")
        
    listaUsuarios.append([id, [diaFecha, mesFecha, añoFecha], rol])
    input("Pulsa ENTER para continuar")
    
#recorre la lista y muestra todos los usuarios
def mostrarUsuarios():
    for user in listaUsuarios:
        print(user)
    input("Pulsa ENTER para continuar")

#pide un ID y le da la opcion de modificar la fecha o el rol
def modificarUsuarios():
    buscarID = int(input("Introduce el ID a buscar: "))
    
    for user in listaUsuarios:
        if user[0] == buscarID:
            idUsuarioLista = user[0] - 1
            print("Ha elegido modificar el usuario : {0}".format(user[0]))
            print("0.- Nada")
            print("1.- Modificar fecha")
            print("2.- Modificar rol")
            modificar = int(input("Que quieres modificar? [0/1/2]: "))
            if modificar == 0:
                print("Saliendo")
                break;
            
            elif modificar == 1:
                diaFecha = int(input("Introduce el dia: "))
                mesFecha = int(input("Introduce el mes: "))
                añoFecha = int(input("Introduce el año: "))
                
                listaUsuarios[idUsuarioLista][1][0] = diaFecha
                listaUsuarios[idUsuarioLista][1][1] = mesFecha
                listaUsuarios[idUsuarioLista][1][2] = añoFecha
                
                print("Fecha nueva: {0}".format(listaUsuarios[idUsuarioLista][1]))
                
                print("**** CLIENTE MODIFICADO CON ÉXITO ***")
            
            elif modificar == 2:
                rol = input("Introduce el rol: ")
                listaUsuarios[idUsuarioLista][2] = rol
                
                print("Rol nuevo: {}".format(listaUsuarios[idUsuarioLista][2]))
                
                print("**** CLIENTE MODIFICADO CON ÉXITO ***")  
                
    input("Pulsa ENTER para continuar")
             
#pide un ID, lo busca y si lo encuentra, con confiramación, lo borra de la lista.  
def borrarUsuario():
    buscarID = int(input("Introduce el ID a buscar: "))
    #por cada usuario en la lista
    for user in listaUsuarios:
        #comprueba si el id del usuario es igual al id que se ha introducido por el teclado
        if user[0] == buscarID:
            #sacamos la posicion de ese usuario en la lista que seria el ID - 1
            posUsuarioLista = user[0] - 1
            confirmacion = int(input("Seguro que quieres borrarlo? [1.-SI / 2.-NO] : "))
            if confirmacion == 1:
                listaUsuarios.pop()[posUsuarioLista]
    
    input("Pulsa ENTER para continuar")
                
#muestra solo las fechas de ingreso de los usuarios
def mostrarSoloFechas():
    #por cada usuario en la lista de usuarios, muestra el element 1 que es la fecha
    for user in listaUsuarios:
        print(user[1])
    
    input("Pulsa ENTER para continuar")
                
#comienzo del bucle principal
while continuar != 1:
    
    menu()
    opcion = int(input("Elige una opcion: "))
    if opcion == 0:
        continuar = int(input("Quieres salir? [1-SI / 2-NO]: "))        
    
    if opcion == 1:
        añadirUser(id)
        id += 1        
    
    if opcion == 2:
        mostrarUsuarios()
        
    if opcion == 3:
        modificarUsuarios()   
        
    if opcion == 4:
         borrarUsuario()
         
    if opcion == 5:
        mostrarSoloFechas()
        
    
print(listaUsuarios)
    