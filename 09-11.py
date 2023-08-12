# rute = "datos.txt"
# rute2 = "nuevosdatos.txt"

# def read_file():
#     x = open(rute, "r", encoding="utf-8")
#     data = x.readlines()
#     x.close()
#     return data

# def calculate_av(data):
#     new_data = []
#     for x in data:
#         y = x.strip().split(",")
#         numbers = [int(value) for value in y[1:]]
#         average = sum(numbers)/len(numbers)
#         modify = x.strip() + f"**{round(average,2)}" + "\n"
#         new_data.append(modify)
#     return new_data

# def write_file(data):
#     x = open(rute2, "w", encoding="utf-8")
#     x.writelines(data)
#     x.close()
#     input("\ntodo funciona de maravilla")

# data = read_file()
# new_data = calculate_av(data)
# write_file(new_data)

x = open("datos.txt", "r", encoding="utf-8")
data = x.readlines()
new_data = []
for x in data:
    y = x.strip().split(",")
    numbers = [int(value) for value in y[1:]]
    average = sum(numbers)/len(numbers)
    modify = x.strip() + f"**{round(average,2)}" + "\n"
    new_data.append(modify)
x = open("datos.txt", "w", encoding="utf-8")
x.writelines(new_data)
x.close()