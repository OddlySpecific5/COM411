import os
import sys
import time
import random


gameLoop = True # this is a boolean which helps the while loop to run
array = [["#","#","#","#","#","#","#","#","#","#"],
        ["#","0"," "," "," "," "," "," ","0","#"],
        ["#"," "," "," "," ","O"," "," "," ","#"],
        ["#","#","#","-","-","-","-","-","#","#"]]

class Player:# Player object ina  class structure
    def __init__(self, playerHealth, playerName, playerPower, playerRegen):
        self.health = playerHealth#
        self.name = playerName
        self.power = playerPower
        self.regen = playerRegen

p1 = Player(100, "Cole", 100, 3) # The default name is my name

class Robot: #Robot object in a class structure
    def __init__(self, health):
        self.health = health

r1 = Robot(100) #r1 is the "name" of the object, for the robot

def draw_robot(array):
   if r1.health >= 50:
       for i in range(0, 4):
           for j in range(1, 2):
               print(array[i])
   print("Beep Boop!!!")



def draw_HUD():# draws the players HUD
    playerArray = [["-", "-", "-", "-", "-", "-"],
                   ["-", "Name: ", "Health:", "Power:", "Regens: ", "-"],
                   ["-", p1.name, p1.health, p1.power, p1.regen, "-"],
                   ["-", "-", "-", "-", "-", "-"]]

    print(2 * "\n")
    print("Player stats: ")
    for i in range(0, 3):
        print(playerArray[i])

    print(1 * "\n")
    print("Robot health: ", r1.health) # shows the robot's health

def attack_Robot():#this method is the one that is used to attack the robot
    randomNumber = random.randrange(1,25)# In theory I don't even need to keep reprogramming this BUT
    #I need different RNG simply because they serve different purposes
    r1.health = r1.health - randomNumber

def Robot_ReturnAttack():#this allows the robot to attack after the player. the robot CAN do 0 damage :):
    randomNumber = random.randrange(0, 10)
    if randomNumber == 0:
        print("The Robot has missed!!!")
    else:
        print("The robot has gone on the attack!!! ...... ")
        p1.health = p1.health - randomNumber


def player_Regen():# If the player types "Regen", it will regen the players health from an amount between the minimum and the maximum:
    if p1.regen > 0 and p1.health < 100:
        p1.regen = p1.regen - 1
        randomNumber = random.randrange(1, 10)
        p1.health = p1.health + randomNumber
        print("The Player has gained ", randomNumber, "Amount of health!!!")
    else:
        print(" you have 0 regens left!! ")

def game_overChecker(): # constantly checks if the player has reached 0health
    if p1.health <= 0:
        print(100*"\n")
        print("Game over.... you died")
        time.sleep(5)
        main_gameLoop() # if so, the game will restart


def variable_reset():# as per title, it resets the var[iables] when the game reset
    p1.health = 100
    p1.power = 100
    r1.health = 100

def main_gameLoop():## maingame loop
    answer1 = input("Are you ready?: ")
    if answer1 == "y" or answer1 == "yes" or  answer1 == "Yes" or answer1 == "YES":
        Username = input("Please enter your name : " )
        p1.name = Username
        variable_reset()  # resets the variables
        time.sleep(.5)
        draw_robot(array)
        time.sleep(.5)
        while gameLoop == True:
            draw_HUD()
            game_overChecker()
            playerChoice = input("What is your next move? Attack|Regen| : ")
            if playerChoice == "Attack" or  playerChoice == "A" or playerChoice == "a":
                attack_Robot()
                Robot_ReturnAttack()
            if playerChoice == "Regen" or  playerChoice == "R" or playerChoice == "r":
                player_Regen()
            else:
                print()

    else:
        sys.exit()



main_gameLoop()