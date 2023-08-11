import os

def poblarIniciales(empleados):
    empleados.append({
        "documento": 1,
        "nombre": "Howard",
        "edad": 25,
        "eps": "Sura"
    })

    empleados.append({
        "documento": 2,
        "nombre": "Nahomi",
        "edad": 33,
        "eps": "Solsalud"
    })
    empleados.append({
        "documento": 3,
        "nombre": "Sarita",
        "edad": 21,
        "eps": "SinergiaSalud"
    })
    empleados.append({
        "documento": 4,
        "nombre": "Juliana",
        "edad": 17,
        "eps": "La EPS de SUBIDA"
    })
    


def validarInput(mensaje):
    data = input(mensaje)
    while(data.strip() == ''):
        print("\nIngrese algún dato\n")
        data = input(mensaje)
    return data

def validaDocumento(id, empleados):
    for i in range(len (empleados)):
        if (empleados[i]['documento'] == id):
            return True
    return False

def ingresarDatos():
    os.system('clear')

    documento = validarInput("Digite el Documento: ")
    while(validaDocumento(documento,empleados)):
        print("\nEl documento ya existe\n")
        documento = validarInput("Digite el Documento: ")
        
    nombre = validarInput("Digite el Nombre: ")
    edad = validarInput("Digite el Edad: ")
    eps = validarInput("Digite el EPS: ")

    empleados.append({
        "documento": documento,
        "nombre": nombre,
        "edad": edad,
        "eps": eps
    })


def eliminarRegistro():
    os.system('clear')
    
    doc = input('Ingrese el documento que desea eliminar')

    for i in range(len(empleados)):
        if(empleados[i]['documento'] == doc):
            name = empleados[i]["nombre"]
            empl = empleados.pop(i)
            return print("\nSe ha eliminado el registro de ", name, '\n')

    return print('\nNo existe el registro con ese documento\n')

def mostrarRegistro():
    os.system('clear')
    
    doc = input('Ingrese el documento que desea mostrar')

    for i in range(len(empleados)):
        if(empleados[i]['documento'] == doc):
            name = empleados[i]["nombre"]
            print("{:<1} {:<15} {:<1} {:<15} {:<1} {:<10} {:<1} {:<18} {:<1}".format("|",empl["documento"], "|", empl["nombre"], "|", empl["edad"], "|", empl["eps"], "|"))
            input("\nPresione cualquier tecla para continuar")
    return print('\nNo existe el registro con ese documento\n')
    input("\nPresione cualquier tecla para continuar")

def reportarListado():
    os.system('clear')
    print("Listado de registros\n")
    print("-"*71)
    print("{:<1} {:<15} {:<1} {:<15} {:<1} {:<10} {:<1} {:<18} {:<1} ".format("|", "Identificacion", "|", "Nombre", "|", "Edad", "|", "EPS", "|"))
    print("|", "-"*67, "|")
    for empl in empleados:
        print("{:<1} {:<15} {:<1} {:<15} {:<1} {:<10} {:<1} {:<18} {:<1}".format("|",empl["documento"], "|", empl["nombre"], "|", empl["edad"], "|", empl["eps"], "|"))
    print("-"*71)
    input("\nPresione cualquier tecla para continuar")

def menu():
    seguir = True
    while seguir:
        os.system('clear')
        print("Menu".center(40," "))
        print("Selecciona la opción que desee")
        print(" "*6 + "1) Ingresar un nuevo registro")
        print(" "*6 + "2) Eliminar un registro")
        print(" "*6 + "3) Mostrar listado total")
        print(" "*6 + "4) Buscar y mostrar un registro")  #****
        print(" "*6 + "5) Actualizar un registro")  #****
        print(" "*6 + "6) Salir del Programa\n")  #****
        print()

        opcion = int(input('opcion -> '))

        if(opcion == 6):
            seguir = False
            return print('\nFin del programa\n')

        if(opcion < 1 or opcion > 6):
            return print('\nEl número debe ser entre 0 y 6\n')

        switch = { 1: ingresarDatos, 2: eliminarRegistro, 3: reportarListado, 4:mostrarRegistro }

        switch[opcion]()
empleados = []
poblarIniciales(empleados)
menu()