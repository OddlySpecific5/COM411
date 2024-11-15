class Robot:
    def __init__(self, RobotName, RobotAge, RobotEnergy, RobotMax_energy):
        self.name = RobotName
        self.age = RobotAge
        self.energy = RobotEnergy
        self.max_energy = RobotMax_energy

    def display_Robot_name(self):
        print(f"I am {robot.name}")  # prints the name


if (__name__ == "__main__"):
    robot = Robot("Robot", 0, 100, 100)
    robot.display_Robot_name()