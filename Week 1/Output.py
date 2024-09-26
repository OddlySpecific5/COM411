import os
import sys
import time
import random

from docutils.io import Input
from pyloco import system
from virtualenv.discovery.cached_py_info import clear


gameLoop = True
array = [["#","#","#","#","#","#","#","#","#","#"],
        ["#","O"," "," "," "," "," "," ","O","#"],
        ["#"," "," "," "," "," "," "," "," ","#"],
        ["#","#","#","-","-","-","-","-","#","#"]]



array2 = [["#","#","#","#","#","#","#","#","#","#"],
        ["#","X"," "," "," "," "," "," ","O","#"],
        ["#"," "," "," "," "," "," "," "," ","#"],
        ["#","#","#","-","-","-","-","-","#","#"]]


class Player:
    def __init__(self, playerHealth, playerName, playerPower):
        self.health = playerHealth#
        self.name = playerName
        self.power = playerPower

p1 = Player(100, "Cole", 100)

class Robot:
    def __init__(self, health):
        self.health = health

r1 = Robot(100)

def draw_robot(array, array2):
   if r1.health >= 50:
       for i in range(0, 4):
           for j in range(1, 2):
               print(array[i])
   else:
       for i in range(0, 4):
           for j in range(1, 2):
               print(array2[i])

def drawHUD():
        print(p1.name)
        print("Hearts: ",  p1.health)
        print("Powerlevel: ","\n", p1.power, "%")
        print("Robot Health: ", "\n", r1.health)


def attackRobot():#this method is the one that is used to attack the robot
    randomNumber = random.randrange(1,10)
    r1.health = r1.health - randomNumber

def RobotReturnAttack():
    print("\n" * 100)
    print("The robot has gone on the attack!!! ...... ")
    time.sleep(2)
    randomNumber = random.randrange(1, 10)
    p1.health = p1.health - randomNumber

    if randomNumber == 0:
        print("The Robot has missed!!!")


def playerRegen():
    randomNumber = random.randrange(1, 10)
    p1.health = p1.health + randomNumber
    print("The Player has gained ", randomNumber,"Amount of health!!!")



answer1 = input("Are you ready?: ")
if answer1 == "y":
        print("\n" * 100)
        time.sleep(.5)
        draw_robot(array,array2)
        time.sleep(1.5)
        drawHUD()
        while gameLoop == True:
            playerChoice = input("What is your next move? Attack|Regen|Dodge : ")
            if playerChoice == "Attack":
                draw_robot(array,array2)
                attackRobot()
                RobotReturnAttack()
                draw_robot(array, array2)
                drawHUD()
            if playerChoice == "Regen" and p1.health != 100:
                draw_robot(array,array2)
                playerRegen()
                drawHUD()




else:
        sys.exit()


