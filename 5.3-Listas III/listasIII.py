continuar = "s"
listaUsuarios = []
id = 1

#muestra las opciones del menu
def menu ():
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
    
#recorre la lista y muestra todos los usuarios
def mostrarUsuarios():
    for user in listaUsuarios:
        print(user)

#pide un ID y le da la opcion de modificar la fecha o el rol
def modificarUsuarios():
    buscarID = int(input("Introduce el ID a buscar: "))
    
    for user in listaUsuarios:
        if user[0] == buscarID:
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
                
                listaUsuarios[user][1][0] = diaFecha
                listaUsuarios[user][1][1] = mesFecha
                listaUsuarios[user][1][2] = añoFecha
                
                print("Fecha nueva: {0}".format(listaUsuarios[user][1]))
                
                print("**** CLIENTE MODIFICADO CON ÉXITO ***")
            
            elif modificar == 2:
                rol = input("Introduce el rol: ")
                listaUsuarios[user][2] = rol
                
                print("Rol nuevo: {}".format(listaUsuarios[user][2]))
                
                print("**** CLIENTE MODIFICADO CON ÉXITO ***")
                
                
                
                
            

while continuar == "s":
    menu()
    opcion = int(input("Elige una opcion: "))
    if opcion == 1:
        añadirUser(id)
        id += 1
    
    if opcion == 2:
        mostrarUsuarios()
        
    if opcion == 3:
        modificarUsuarios()    
    
print(listaUsuarios)
    