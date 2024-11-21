class Robot:
    def __init__(self):
        self.name = "Robot"
        self.age = 0
        self.energy = 100
        self.max_energy = 100

    def __repr__(self):
        return f"{robot.name} / {robot.age}"

    def display_Robot_name(self):
        print(f"I am {robot.name}")  # prints the name

    def display_Robot_age(self):
        print(f"I am {robot.age}")

    def display_Human_energy(self):
        print(f"{robot.name} has {robot.energy}% left")

    def grow(self):
        robot.age +=1


    def eat(self, amount):
        if robot.energy >= robot.max_energy:  # bigger or equal to just to avoid any outliers e.g. if the energy is == to 102
            print("Energy is already full!!")
        else:
            robot.energy += amount

    def distance(self, distance):
        robot.energy -= distance  # lets assume 100-102 = -2
        if robot.energy < 0:
            tempHolder = robot.energy  # storing the difference value incase in need of later
            robot.energy -= robot.energy  # -2 - -2 = 0
            print(f"Testing {robot.name} energy {robot.energy} left")
            print(tempHolder)  ## Debugging
            # logic goes here
        else:
            print(f"You have {robot.energy}% left!!")

robot = Robot()

