import os
import sys
import time
import random


gameLoop = True
array = [["#","#","#","#","#","#","#","#","#","#"],
        ["#","0"," "," "," "," "," "," ","0","#"],
        ["#"," "," "," "," ","O"," "," "," ","#"],
        ["#","#","#","-","-","-","-","-","#","#"]]





class Player:# Player object
    def __init__(self, playerHealth, playerName, playerPower, playerRegen):
        self.health = playerHealth#
        self.name = playerName
        self.power = playerPower
        self.regen = playerRegen

p1 = Player(100, "Cole", 100, 3)





class Robot: #Robot object
    def __init__(self, health):
        self.health = health

r1 = Robot(100)

def draw_robot(array):
   if r1.health >= 50:
       for i in range(0, 4):
           for j in range(1, 2):
               print(array[i])


def drawHUD():# draws the players HUD


    playerArray = [["-", "-", "-", "-", "-", "-"],
                   ["-", "Name: ", "Health:", "Power:", "Regens: ", "-"],
                   ["-", p1.name, p1.health, p1.power, p1.regen, "-"],
                   ["-", "-", "-", "-", "-", "-"]]

    print(2 * "\n")
    print("Player stats: ")
    for i in range(0, 3):
        print(playerArray[i])

    print(1 * "\n")
    print("Robot health: ", r1.health)

def attackRobot():#this method is the one that is used to attack the robot
    randomNumber = random.randrange(1,25)
    r1.health = r1.health - randomNumber

def RobotReturnAttack():#this allows the robot to attack after the player. the robot CAN do 0 damage :):
    randomNumber = random.randrange(1, 25)
    if randomNumber == 0:
        print("The Robot has missed!!!")
    else:
        print("The robot has gone on the attack!!! ...... ")
        p1.health = p1.health - randomNumber


def playerRegen():# If the player types "Regen", it will regen the players health from an amount between 1 and 20:
    if p1.regen > 0:
        p1.regen = p1.regen - 1
        randomNumber = random.randrange(1, 10)
        p1.health = p1.health + randomNumber
        print("The Player has gained ", randomNumber, "Amount of health!!!")
    else:
        print(" you have 0 regens left!! ")

def game_overChecker():
    if p1.health <= 0:
        print(100*"\n")
        print("Game over.... you died")
        time.sleep(5)
        main_gameLoop()


def variable_reset():
    p1.health = 100
    p1.power = 100

    r1.health = 100

def main_gameLoop():
    answer1 = input("Are you ready?: ")
    if answer1 == "y":
        Username = input("Please enter your name : " )
        p1.name = Username
        variable_reset()  # resets the variables
        time.sleep(.5)
        draw_robot(array)
        time.sleep(.5)
        while gameLoop == True:
            drawHUD()
            game_overChecker()
            playerChoice = input("What is your next move? Attack|Regen| : ")
            if playerChoice == "Attack":
                attackRobot()
                RobotReturnAttack()
            if playerChoice == "Regen" and p1.health != 100:
                playerRegen()
    else:
        sys.exit()





main_gameLoop()