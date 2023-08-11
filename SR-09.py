import os

students = {}

def verify_Input(mensaje):
    data = input(mensaje)
    while(data.strip() == ''):
        print("\nIngrese algún dato\n")
        data = input(mensaje)
    return data


def add_student():
    print("INGRESO DE ESTUDIANTE")
    code = verify_Input("Ingrese la ID del estudiante: ")
    name = verify_Input("Ingrese el nombre completo del estudiante: ")
    notes = []
    for x in range(3):
        note = verify_Input(f"Ingrese la {x} nota: ")
        notes.append(note)
    students[code] = {"name": name, "notes":notes}
    print("Los datos han sido ingresados correctamente")
    input("\nPresione cualquier tecla para volver")

def browse_students():
    print("BUSQUEDA DE ESTUDIANTE")
    code = verify_Input("Ingrese la ID del estudiante: ")
    print("")
    for x in students.keys():
        if x == code:
            name = students[x]["name"]
            print("-"*30,f"\nCodigo del estudiante: {code}")
            print(f"Nombre del estudiante: {name}")
            print(f"Notas del estudiante: ", end=" ")
            for y in students[x]["notes"]:
                print(y, end=", ")
            return input("\nPresione cualquier tecla para volver")
    
    print("No se encontro el estudiante")
    input("\nPresione cualquier tecla para volver")

def update_data_student():
    print("ACTUALIZAR DATOS DE ESTUDIANTE")
    code = verify_Input("Ingrese la ID del estudiante: ")
    for x in students.keys():
        if x == code:
            print("Que datos quiere actualizar?\n1. Nombre\n2. Notas\n3. Salir al menu")
            op = int(input('opcion -> '))
            if op == 1:
                name = verify_Input("Ingrese el nuevo nombre completo del estudiante: ")
                students[code]["name"] = name
            if op == 2:
                notes = []
                for x in range(3):
                    note = verify_Input(f"Ingrese la {x} nota: ")
                    notes.append(note)
                students[code]["notes"] = notes
            if op == 3:
                return input("\nPresione cualquier tecla para volver")
    print("No se encontro el estudiante")
    input("\nPresione cualquier tecla para volver")

def delete_student():
    print("BORRAR ESTUDIANTE")
    code = verify_Input("Ingrese la ID del estudiante: ")
    for x in students.keys():
        if x == code:
            students[x].pop()
            print(f"La informacion del estudiante {code} ha sido eliminada")
    
    print("No se encontro el estudiante")
    input("\nPresione cualquier tecla para volver")

def calculate_definity():
    print("CALCULAR DEFINITIVA DE LOS ESTUDIANTE")
    print("Se calcularán las definitivas de los estudiantes...")
    input("Presione cualquier tecla para continuar...")
    for x in students.keys():
        notes = students[x]["notes"]
        prom = (sum(notes)/len(notes))
        students[x]["average"] = prom
    print("Las notas definitivas ya se han calculado")
    input("\nPresione cualquier tecla para volver")


def show_general():
    print("LISTA GENERAL DE ESTUDIANTES")
    print("\nCODIGO\tESTUDIANTE\tDEFINITIVA")
    for x in students.keys():
        name = students[x]["name"]
        note = students[x]["average"]
        print(f"{x}\t{name}\t{note}")

def main_menu():
    seguir = True
    while seguir:
        os.system('clear')
        print("Menu".center(40," "))
        print("Selecciona la opción que desee")
        print(" "*6 + "1) Agregar un nuevo registro")
        print(" "*6 + "2) Buscar un estudiante")
        print(" "*6 + "3) Actualizar datos del Estudiante")
        print(" "*6 + "4) Borrar un estudiante")  
        print(" "*6 + "5) Calcular notas definitivas")  
        print(" "*6 + "6) Listar con definitivas y promedio general")  
        print(" "*6 + "7) Salir del Programa\n")  
        print()
        option = int(input('opcion -> '))
        if(option == 7):
            seguir = False
            return print('\nFin del programa\n')
        if(option < 1 or option > 7):
            return print('\nEl número debe ser entre 0 y 7\n')

        options = {1: add_student, 2: browse_students, 3: update_data_student, 4:delete_student, 5:calculate_definity, 6:show_general}
        options[option]()

main_menu()