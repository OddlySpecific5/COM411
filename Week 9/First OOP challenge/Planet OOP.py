import Human, Robot

class Planet:
    def __init__(self, name):
        self.inhabitants= {'Humans' : [], 'Robots': []}
        self.name = name



    def add_human(self, human):
        planet.inhabitants["Humans"].append(human)

    def remove_human(self):
        pass

    def add_robot(self):
        pass

    def remove_robot(self):
        pass


planet = Planet("Earth")

if (__name__ == "__main__"):
    while True:
        name = input("Say a name")
        age = int(input("State an age"))
        h1 = Human(name, age)

        planet.add_human(h1)
        print(planet.inhabitants["Humans"])