contacts = {}
def ingreso():
    print("\nIngreso de contactos")
    while True:
        x = input("Ingrese el nombre: ")
        if x in contacts:
            print("Digite un nombre que no este registrado\n")
            continue
        y = int(input("Ingrese el numero de telefono: "))
        if y in contacts.values():
            print("Digite un telefono que no este registrado\n")
            continue
        else:
            contacts[x] = y
            break
    print("\n", contacts,"\n")

def menu():
    while True:
        ingreso()
        print("\nQuieres ingresar otro contacto?\n1. Si   2. No")
        option = int(input("Opcion: "))
        if option == 2:
            print("Contactos ingresados: ", contacts.items(),"\n")
            break
    print("\nGracias por usar el programa")

menu()