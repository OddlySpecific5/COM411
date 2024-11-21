class Human:
    def __init__(self):
        self.name = "Human"
        self.age = 0
        self.energy = 100
        self.max_energy = 100

    def __repr__(self):
        return f"{human.name} / {human.age}"

    def display_Human_name(self):
        print(f"I am {human.name}")  # prints the name

    def display_Human_age(self):
        print(f"I am {human.age}")  # prints the age

    def display_Human_energy(self):
        print(f"{human.name} has {human.energy}% left")  # prints the energy percentage

    def grow(self):
        human.age +=1

    def eat(self, amount):
        if human.energy >= human.max_energy:# bigger or equal to just to avoid any outliers e.g. if the energy is == to 102
            print("Energy is already full!!")
        else:
            human.energy += amount

    def distance(self, distance):
        human.energy -= distance# lets assume 100-102 = -2
        if human.energy < 0:
            tempHolder = human.energy # storing the difference value incase in need of later
            human.energy -= human.energy # -2 - -2 = 0
            print(f"Testing {human.name} energy {human.energy} left")
            print(tempHolder) ## Debugging purposes
        else:
            print(f"You have {human.energy}% left!!")





human = Human()

