subjects = []
student = {}

def add_subjects():
    print("AÑADIR ASIGNATURA")
    name = input("Ingrese el nombre de la asignatura: ")
    subjects.append(name)
    print(f"")
    input("\nPresione cualquier tecla para volver")

def add_note():
    print("Ingresar nota\nDigite el numero de la asignatura")
    counter = 1
    for x in subjects:
        print(counter, " -> ", x)
        counter += 1
    y = int(input("Opcion: "))
    index = y-1
    subject = subjects[index]
    note = int(input(f"Digite la nota de {subject}: "))
    student[subject] = note
    input("\nPresione cualquier tecla para volver")

def print_notes():
    print("Mostrar notas")
    for x in student.items():
        print(f"\nAsignatura: {x[0]}\t Nota: {x[1]}")
    input("\nPresione cualquier tecla para volver")

def menu():
    while True:
        print("MENU \n1. Ingresar asignatura \n2. Ingresar nota a la asignatura \n3. Mostrar notas\n4. Salir")
        option = int(input("Opcion: "))
        if option == 1:
            add_subjects()
        elif option == 2:
            add_note()
        elif option == 3:
            print_notes()
        elif option == 4:
            break
        else:
            print("Digite una opcion valida")
        print(student)
        print(subjects)
    print("\nGracias por usar el programa")

menu()