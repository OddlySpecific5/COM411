class Human:
    def __init__(self, HumanName, HumanAge, HumanEnergy, HumanMax_energy):
        self.name = HumanName
        self.age = HumanAge
        self.energy = HumanEnergy
        self.max_energy = HumanMax_energy

    def display_Human_name(self):
        print(f"I am {human.name}")  # prints the name


if (__name__ == "__main__"):
    human = Human("Human", 0, 100, 100)
    human.display_Human_name()