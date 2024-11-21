from human import Human
from robot import  Robot
import random

class Planet:
    def __init__(self, name):
        self.inhabitants= {'Humans' : [], 'Robots': []}
        self.name = name


    def __str__(self):
        return f"Name of planet = {self.name}"

    def __repr__(self):
        return f"Name of planet = {self.name}"

    def add_human(self, human):
        planet.inhabitants["Humans"].append(Human)

    def remove_human(self, human):
        planet.inhabitants["Humans"].remove(Human)

    def add_robot(self, robot):
        planet.inhabitants["Robots"].append(Robot)

    def remove_robot(self, robot):
        planet.inhabitants["Robots"].remove(Robot)


planet = Planet("Earth")



class Universe:
    def __init__(self):
        self.planets = []


    def generate(self):
        p1 = Planet("Earth")
        randomNum = random.randint(1, 100)
        for i in range(randomNum):
            universe.planets.append(Human())
        print(universe.planets)


if (__name__ == "__main__"):
    universe = Universe()
    universe.generate()
    print(universe.planets)