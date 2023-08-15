import json, os

def read_data():
    print("Lectura de datos")
    with open("json/Ahorradores.json", "r", encoding="UTF-8") as x:
        data = json.load(x)
    input("Los datos han sido cargados exitosamente")
    return data
    
def show_data():
    print("Mostrar datos")
    for x in data["cliente"]:
        print("Identificacion: ", x["Id"])
        print("Nombre", x["Nombre"])
        print("Numero de cuenta", x["NumCuenta"])
        print("Saldo en la cuenta", "$", x["Saldo"])
        print("-"*40)
    input("Presiona cualquier tecla para volver")

def file_dian():
    print("Crear archivo DIAN")
    data_dian = []
    counter = 1
    for x in data["cliente"]:
        users_dian = {}
        print(x)
        balance = x["Saldo"]
        print(balance)
        if balance > 35000000:
            users_dian["consecutivo"] = counter
            users_dian["numCuenta"] = x["NumCuenta"]
            users_dian["saldo"] = balance
            counter += 1
            data_dian.append(users_dian)
    print(data_dian)
    input("x")
    with open("json/Dian.json", "w", encoding="UTF-8") as y:
        json.dump(data_dian,y)
    input("Ya se ha creado el archivo")

def main_menu():
    while True:
        os.system("clear")
        print("Administracion Bancaria".center(50, " "))
        print("1. Mostrar datos ingresados\n2. Crear archivo para DIAN\n3. Salir")
        option= int(input("Opcion: "))
        options = {1:show_data, 2:file_dian}
        if option == 3:
            print("Gracias por usar el programa")
            break
        options[option]()

data = read_data()
main_menu()