# import json
# with open("json/services.json", "r") as employees:
#     data = json.load(employees)
#     for user in data["users"]:
#         print("Full name: ", user["full_name"])
#         print("Email: ", user["email"])
#         print("ID number: ", user["id"])
#         print("Total packages: ", user["total_packages"])
#         print("Total price: ", user["total_price"])

import json, os

data = {}
while True:
    os.system("clear")
    print("Datos ingresados ", len(data))
    name = input("Ingrese el nombre: ")
    age = int(input("Ingrese la edad: "))
    weight = int(input("Ingrese el peso: "))
    data[name] = {"edad":age, "peso":weight}
    print("\nQuieres ingresar otro jugador?\n1. SI\n2. NO")
    option = int(input("Option: "))
    if option == 2:
        break

with open("json/jugadores.json", "w") as x:
    json.dump(data,x)