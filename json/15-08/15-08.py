import json, os

def read_data():
    with open("a/PetShopping.json", "r", encoding="UTF-8") as x:
        data = json.load(x)
        return data

def write_data(data):
    with open("a/PetShopping.json", "w", encoding="UTF-8") as x:
        json.dump(data,x, indent=4)
        print("Datos guardados en disco!")

def show_data():
    pets = read_data()
    print("Mostrar mascotas\n")
    print("{:<3} {:<1} {:<10} {:<1} {:<15} {:<1} {:<10} {:<1} {:<35} {:<1}".format(" ", "|", "TIPO", "|", "RAZA", "|", "PRECIO", "|", "SERVICIOS", "|"))
    counter = 1
    for x in pets["pets"]:
        services = ""
        for y in x["servicios"]:
            services = str(services) + str(y) + ", " 
        print("{:<3} {:<1} {:<10} {:<1} {:<15} {:<1} {:<10} {:<1} {:<35} {:<1}".format(str(counter), "|", x["tipo"], "|", x["raza"], "|", x["precio"], "|", services.title().rstrip(", "), "|"))
        counter += 1
    input("\nPresione cualquier tecla para continuar")

def add_pet():
    pets = read_data()
    print("Agregar mascotas\n")
    while True:
        kind = input("Ingrese el tipo de mascota: ")
        race = input("Ingrese la raza de la mascota: ")
        size = input("Ingrese el tamaño de la mascota: ")
        price = int(input("Ingrese el precio de la mascota: "))
        services = []
        print("Ingreso de servicios")
        while True:
            x = input("Ingrese el nombre del servicio: ")
            services.append(x)
            option = int(input("Quieres ingresar otro servicio?\n1. SI\n2. NO\n-> "))
            if option == 2:
                break
        pets["pets"].append({"tipo": kind.title(), "raza": race.title(), "talla": size.title(), "precio": price, "servicios": services})
        print("\nDatos completos ingresados\nQuieres ingresar otra mascota? ")
        option = int(input("\n1. SI\n2. NO\n-> "))
        if option == 2:
            break
        os.system("clear")
    write_data(pets)
    input("\nPresione cualquier tecla para continuar")

def show_pets_type():
    pets = read_data()
    print("\nMostrar mascotas por tipo\n\nElige el tipo de mascota\n")
    counter = 0
    y = []
    for x in pets["pets"]:
        y.append(x["tipo"])
    y = set(y)
    for x in y:
        print((counter+1), " -> ", x)
        counter += 1
    option = int(input("Opcion: "))
    y = list(y)
    option = y[option-1]
    print("{:<15} {:<1} {:<10} {:<1} {:<35} {:<1}".format("RAZA", "|", "PRECIO", "|", "SERVICIOS", "|"))
    for x in pets["pets"]:
        if x["tipo"] == option:
            services = ""
            for y in x["servicios"]:
                services = str(services) + str(y) + ", " 
            print("{:<15} {:<1} {:<10} {:<1} {:<35} {:<1}".format(x["raza"], "|", str(x["precio"]), "|", services.title().rstrip(", "), "|"))
            counter += 1
    input("\nPresione cualquier tecla para continuar")

def update_data():
    pets = read_data()
    print("\nActualizar datos de una mascota\nElige cual mascota vas a actualizar\n")
    counter = 1
    print("{:<3} {:<15} {:<1} {:<10}".format(" " ,"TIPO", "|", "RAZA"))
    for x in pets["pets"]:
        print("{:<3} {:<15} {:<1} {:<10}".format(counter, x["tipo"], "|", x["raza"]))
        counter += 1
    indice = int(input("Opcion: "))
    print("\nQue quieres modificar de la mascota\n1. Raza\n2. Talla\n3. Precio\n4. Salir")
    option = int(input("Opcion: "))
    if option == 1:
        race = input("Ingrese la nueva raza: ")
        pets["pets"][indice-1]["raza"] = race
    if option == 2:
        size = input("Ingrese la nueva talla: ")
        pets["pets"][indice-1]["talla"] = size
    if option == 3:
        price = int(input("Ingrese el nuevo precio: "))
        pets["pets"][indice-1]["precio"] = price
    else:
        return input("Volveras al menu principal") 
    write_data(pets)

def delete():
    pets = read_data()
    print("\Eliminar datos de una mascota\nElige cual mascota vas a eliminar\n")
    counter = 1
    print("{:<3} {:<15} {:<1} {:<10}".format(" " ,"TIPO", "|", "RAZA"))
    for x in pets["pets"]:
        print("{:<3} {:<15} {:<1} {:<10}".format(counter, x["tipo"], "|", x["raza"]))
        counter += 1
    indice = int(input("Opcion: "))
    pets["pets"].pop(indice-1)
    write_data(pets)
    input("Los datos han sido eliminados correctamente")

def main_menu():
    while True:
        os.system("clear")
        print("Administracion de Mascotas\n")
        print("\n1. Mostrar datos\n2. Añadir mascota\n3. Mascotas por tipo\n4. Actualizar datos\n5. Eliminar mascota\n6. Salir")
        options = {1:show_data, 2:add_pet, 3:show_pets_type, 4:update_data, 5:delete}
        option = int(input("opcion: "))
        if option == 6:
            print("Gracias por usar el programa")
            break
        os.system("clear")
        options[option]()
        
main_menu()
