continuar = "s"
listaUsuarios = []
id = 1

def menu ():
    print("1.- Añadir usuario")
    print("2.- Mostrar todos los usuarios")
    print("3.- Modificar usuarios dado un ID")
    print("4.- Borrar usuario dado un ID")
    print("5.- Mostrar solo las fechas")
    
def añadirUser(id):
    diaFecha = int(input("Introduce el dia: "))
    mesFecha = int(input("Introduce el mes: "))
    añoFecha = int(input("Introduce el año: "))
        
    rol = input("Rol del usuario: [usuario, usuario avanzado, admin]: ")
        
    listaUsuarios.append([id, [diaFecha, mesFecha, añoFecha], rol])
    


while continuar == "s":
    menu()
    opcion = int(input("Elige una opcion: "))
    if opcion == 1:
        añadirUser(id)
        id += 1
    
print(listaUsuarios)
    