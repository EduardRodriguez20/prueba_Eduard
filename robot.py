# Creamos el diccionario de los colores para identificar cada robot
colors = {
    "Black": "\x1b[90m",
    "Blue": "\x1b[94m",
    "Cyan": "\x1b[96m",
    "Green": "\x1b[92m",
    "Magenta": "\x1b[95m",
    "Red": "\x1b[91m",
    "White": "\x1b[97m",
    "Yellow ": "\x1b[93m",
}

# Creamos el arte del robot con las llaves correspondientes a los atributos de
# cada parte del robot y poderlas modificar
robot_art = r"""
      0: {head_name}
      Is available: {head_status}
      Attack: {head_attack}
      Defense: {head_defense}
      Energy consumption: {head_energy_consump}
              ^
              |                  |1: {weapon_name}
              |                  |Is available: {weapon_status}
     ____     |    ____          |Attack: {weapon_attack}
    |oooo|  ____  |oooo| ------> |Defense: {weapon_defense}
    |oooo| '    ' |oooo|         |Energy consumption: {weapon_energy_consump}
    |oooo|/\_||_/\|oooo|
    `----' / __ \  `----'           |2: {left_arm_name}
   '/  |#|/\/__\/\|#|  \'           |Is available: {left_arm_status}
   /  \|#|| |/\| ||#|/  \           |Attack: {left_arm_attack}
  / \_/|_|| |/\| ||_|\_/ \          |Defense: {left_arm_defense}
 |_\/    O\=----=/O    \/_|         |Energy consumption: {left_arm_energy_consump}
 <_>      |=\__/=|      <_> ------> |
 <_>      |------|      <_>         |3: {right_arm_name}
 | |   ___|======|___   | |         |Is available: {right_arm_status}
//\\  / |O|======|O| \  //\\        |Attack: {right_arm_attack}
|  |  | |O+------+O| |  |  |        |Defense: {right_arm_defense}
|\/|  \_+/        \+_/  |\/|        |Energy consumption: {right_arm_energy_consump}
\__/  _|||        |||_  \__/
      | ||        || |          |4: {left_leg_name}
     [==|]        [|==]         |Is available: {left_leg_status}
     [===]        [===]         |Attack: {left_leg_attack}
      >_<          >_<          |Defense: {left_leg_defense}
     || ||        || ||         |Energy consumption: {left_leg_energy_consump}
     || ||        || || ------> |
     || ||        || ||         |5: {right_leg_name}
   __|\_/|__    __|\_/|__       |Is available: {right_leg_status}
  /___n_n___\  /___n_n___\      |Attack: {right_leg_attack}
                                |Defense: {right_leg_defense}
                                |Energy consumption: {right_leg_energy_consump}

"""

# Creamos la clase Robot
class Robot:

    # En el metodo incial creamos 2 variables para ingresar, nombre y el color
    def __init__ (self, name, color_code):
        self.name_attr = name
        self.color_code_attr = color_code
        self.energy = 100      # Declaramos la energia del robot
        self.inventory = []

        # Creamos una lista con objetos de cada parte del robot con sus respectivos
        # atributos para el ataque, la defensa y la energia que consume
        self.parts = [
            Part("Head", attack_level=5, defense_level= 10, energy_consumption= 5),
            Part("Weapon", attack_level=15, defense_level=10, energy_consumption=10),
            Part("Left Arm", attack_level=3, defense_level=20, energy_consumption=40),
            Part("Right Arm", attack_level=6, defense_level=20, energy_consumption=40),
            Part("Left Leg", attack_level=4, defense_level=20, energy_consumption=15),
            Part("Right Leg", attack_level=8, defense_level=20, energy_consumption=15),
        ]

    # Creamos el metodo saludar para mostrar el nombre del robot
    def great (self):
        print ("My name is:", self.name_attr)

    # Creamos el metodo mostrar energia para ir revisando la energia del robot
    def print_energy (self):
        print  ("The remaining energy is:", self.energy)

    # Creamos el metodo ataque con los atributos robot enemigo, parte para usar y
    # parte para atacar
    def attack (self, enemy_robot, part_to_use, part_to_attack):

        # Modifique el codigo para ser mas claros con la instancia, en enemy_part
        # se guarda la parte para atacar del robot enemigo
        enemy_part = enemy_robot.parts[part_to_attack]
        print('==> parte que ataca: ',self.parts[part_to_use].energy_consumption_attr,' self energy: ', self.energy)
        """ if self.parts[part_to_attack].energy_consumption_attr < self.energy: """

        # Teniendo esta variable reducimos su defensa con el ataque de la parte
        # que usa el otro robot y reduce su energia
        enemy_part.defense_level_attr -= self.parts[part_to_use].attack_level_attr
        self.energy -= self.parts[part_to_use].energy_consumption_attr

    # Este metodo valida si tenemos energia en el robot, nos retorna True o False
    def is_on(self):
        return self.energy > 0

    # Este metodo hace una validacion para cada parte con ayuda del ciclo for
    # ayudandose de un metodo is_avaliable de otra clase
    def is_there_avaliable_parts(self):
        for part in self.parts:

            # Si la parte esta disponible la negamos para sacarla del if
            if not part.is_avaliable():
                return False
        return True

    # En este metodo aplicamos el color del robot, mostramos el arte del robot
    # con el formato de cada parte con ayuda del siguiente metodo,
    # tambien el saludo y la energia, al final cambiamos el color original
    def print_status(self):
        print(self.color_code_attr)
        str_robot = robot_art.format(**self.get_part_status())
        self.great()
        self.print_energy()
        print(str_robot)
        print(colors["White"])

    # Este metodo creamos un diccionario vacio y con el ciclo for iteramos en cada
    # parte y actualizamos el diccionario vacio para retornarlo al metodo anterior
    def get_part_status(self):
        part_status = {}
        for part in self.parts:
            status_dict = part.get_status_dict()
            part_status.update(status_dict)
        return part_status


    def detach_part_piece(self, part_index):
        part = self.parts[part_index]

        if part_index == 0:  # Cabeza
            part_piece = PartPiece("synthovisor cortex", attack_bonus=5, duration=1)
        elif part_index in [2, 3]:  # Brazos
            part_piece = PartPiece("cyber module", defense_bonus=5, duration=1)
        elif part_index in [4, 5]:  # Piernas
            part_piece = PartPiece("elemental piece", defense_bonus=9999, duration=1)
        elif part_index == 1:  # Arma
            part_piece = PartPiece("electro arrows", attack_bonus=10, duration=1)
        else:
            return None

        part_piece.apply_bonus(part)
        return part_piece

    def fuse_parts(self):
        if len(self.inventory) == 0:
            print("No tienes piezas de partes en tu inventario.")
            return

        print("Piezas disponibles en tu inventario:")
        for i, part_piece in enumerate(self.inventory):
            print(f"{i + 1}. {part_piece.name}")

        choice = input("Elige una pieza de parte para fusionar: ")
        choice = int(choice) - 1

        if choice < 0 or choice >= len(self.inventory):
            print("Opción inválida.")
            return

        part_piece = self.inventory.pop(choice)

        print("Piezas disponibles para fusionar:")
        for i, part in enumerate(self.parts):
            print(f"{i + 1}. {part.name}")

        part_to_fuse = input("Elige una parte para fusionar con la pieza: ")
        part_to_fuse = int(part_to_fuse) - 1

        if part_to_fuse < 0 or part_to_fuse >= len(self.parts):
            print("Opción inválida.")
            return

        part = self.parts[part_to_fuse]
        part_piece.apply_bonus(part)

        print(f"La parte '{part.name}' ha sido fusionada con '{part_piece.name}'.")

# Creamos la clase Part para crear un objeto por cada parte, anteriormente usados
class Part:
    # Al iniciar solicitamos los datos para ser ingresados en los objetos
    def __init__ (self, name, attack_level, defense_level, energy_consumption):
        self.name_attr = name
        self.attack_level_attr = attack_level
        self.defense_level_attr = defense_level
        self.energy_consumption_attr = energy_consumption

    # Creamos un metodo que aplicara un formato al arte del robot agregando los
    # valores a sus atributos para imprimirlos
    def get_status_dict(self):
        formatted_name = self.name_attr.replace (" ", "_").lower()
        return {
            "{}_name".format(formatted_name): self.name_attr.upper(),
            "{}_status".format(formatted_name): self.is_avaliable(),
            "{}_attack".format(formatted_name): self.attack_level_attr,
            "{}_defense".format(formatted_name): self.defense_level_attr,
            "{}_energy_consump".format(formatted_name): self.energy_consumption_attr,
        }

    # Validamos si la defensa de una parte es mayor a cero, retornamos True
    def is_avaliable(self):
        return self.defense_level_attr > 0

class PartPiece:
    def __init__(self, name, attack_bonus=0, defense_bonus=0, duration=1):
        self.name = name
        self.attack_bonus = attack_bonus
        self.defense_bonus = defense_bonus
        self.duration = duration

    def apply_bonus(self, part):
        # Aplica los bonos de ataque y defensa a una parte específica
        part.attack_level += self.attack_bonus
        part.defense_level += self.defense_bonus

    def remove_bonus(self, part):
        # Remueve los bonos de ataque y defensa de una parte específica
        part.attack_level -= self.attack_bonus
        part.defense_level -= self.defense_bonus


# Creamos la funcion play para iniciar el juego
def play():

    # Damos bienvenida al programa y creamos objetos de los robots con nombre y color
    print("Welcome to the game")
    robot_one = Robot("Jarvis", colors["Cyan"])
    robot_two = Robot("Friday", colors["Red"])

    # Creamos variables para usar en el ciclo while y para la ronda
    playing = True
    rount = 0
    while playing:

        # En esta condicion los resultados seran 0 y 1 para cada turno de los robots
        if rount % 2 == 0:

            # Si el turno es 0 el primer robot sera el actual y el segundo el enemigo
            current_robot = robot_one
            enemy_robot = robot_two
        else:

            # Similar a la anterior instancia solo que inverso para el otro turno
            current_robot = robot_two
            enemy_robot = robot_one

        if not enemy_robot.is_on():
            print("\nCongratulations, has won:", current_robot.name_attr)
            print("The robot enemy has not energy")
            print("Enemy robot status: ")
            enemy_robot.print_status()
            break
        # Teniendo declarados el robot actual y el enemigo solicitamos la parte
        # a usar
        current_robot.print_status()
        print("Which part should i use to attack?")

        #while true si la energia del robot es menor a la parte a usar, sigue en el ciclo para volver a pedir la parte,
        part_to_use = int(input("Choose a number part: "))
        

        # Ahora solicitamos a que parte del robot enemigo atacaremos
        enemy_robot.print_status()
        print("which part of the enemy should attack?")
        part_to_attack = int(input("Choose a enemy part to attack: "))

        # Ejecutamos el metodo attack para el robot actual con los datos solicitados
        current_robot.attack(enemy_robot, part_to_use, part_to_attack)

        # Incrementamos el contador para el siguiente turno
        rount += 1

        # Antes de iniciar el siguiente turno validamos la energia y las partes
        # Si hay una parte sin defensa, o sea dañada, o si se acabo la energia
        # rompemos el ciclo while y mostramos el robot ganador y el estado del
        # robot enemigo

        if not enemy_robot.is_there_avaliable_parts() or not enemy_robot.is_on():
            playing = False
            print("\nCongratulations, has won:", current_robot.name_attr)
            print("Enemy robot status: ")
            enemy_robot.print_status()

# Iniciamos la funcion para iniciar el juego.
play()
