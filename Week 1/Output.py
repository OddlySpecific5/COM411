import sys
import time
import random
from doctest import debug
from operator import truediv
import pygame
import threading

from pygame.examples.music_drop_fade import play_file

pygame.mixer.init()

defeat_sound = pygame.mixer.Sound("Explosion.wav")

background_music = pygame.mixer.Sound("BackgroundMusic.mp3")
background_music.set_volume(.2)

hitEffect_music = pygame.mixer.Sound("hitHurt.wav")

powerup_sfx = pygame.mixer.Sound("powerUp.wav")
powerup_sfx.set_volume(.5)

laser_sfx = pygame.mixer.Sound("laserShoot.wav")
laser_sfx.set_volume(.5)

gameLoop = True # this is a boolean which helps the while loop to run
array = [["#","#","#","#","#","#","#","#","#","#"],
        ["#","0"," "," "," "," "," "," ","0","#"],
        ["#"," "," "," "," ","O"," "," "," ","#"],
        ["#","#","#","-","-","-","-","-","#","#"]]

class Player:# Player object ina  class structure
    def __init__(self, playerHealth, playerName, playerPower, playerRegen):
        self.health = playerHealth
        self.name = playerName
        self.power = playerPower
        self.regen = playerRegen

p1 = Player(100, " ", 100, 3) # The default name is my name

p1healthTemp = p1.health
p1powerTemp = p1.power
p1regenTemp = p1.regen

class Robot: #Robot object in a class structure
    def __init__(self, health):
        self.health = health


r1 = Robot(20) #r1 is the "name" of the object, for the robot
r1healthTemp = r1.health

def variable_reset():# as per title, it resets the var[iables] when the game reset
    p1.health = p1healthTemp
    p1.power = p1powerTemp
    p1.regen = p1regenTemp
    r1.health = r1healthTemp


def draw_robot(array):
    for i in range(0, 4):
          for j in range(1, 2):
              print(array[i])
    print("Beep Boop!!!")# Beep boop


def play_sound_effect(effect):
    # Play the sound effect in a non-blocking way
    effect.play()

def end_message():# typewrites a message
    text = input("What do you want to say to the robot?: ")
    print(p1.name," :", end =" ", flush=True)
    for i in range(0, len(text)):
        print(text[i], end ="", flush=True)
        time.sleep(float(.2))

    print("\n")

def end_message2():# typewrites a message
    text = "You will never defeat me..",p1.name
    print("Robot", " :", end="")
    for i in range(0, len(text)):
        print(text[i], end ="")
        time.sleep(float(.2))

    print("\n")


def title_screen():# typewrites a message
    text = '''⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀

          ██████╗  ██████╗ ██████╗  ██████╗ ████████╗    ██╗  ██╗██╗██╗     ██╗     ███████╗██████╗ 
          ██╔══██╗██╔═══██╗██╔══██╗██╔═══██╗╚══██╔══╝    ██║ ██╔╝██║██║     ██║     ██╔════╝██╔══██╗
          ██████╔╝██║   ██║██║  ██║██║   ██║   ██║       █████╔╝ ██║██║     ██║     █████╗  ██████╔╝
          ██╔═══╝ ██║   ██║██║  ██║██║   ██║   ██║       ██╔═██╗ ██║██║     ██║     ██╔══╝  ██╔══██╗
          ██║     ╚██████╔╝██████╔╝╚██████╔╝   ██║       ██║  ██╗██║███████╗███████╗███████╗██║  ██║
          ╚═╝      ╚═════╝ ╚═════╝  ╚═════╝    ╚═╝       ╚═╝  ╚═╝╚═╝╚══════╝╚══════╝╚══════╝╚═╝  ╚═╝

        '''

    for i in range(0, len(text)):
        print(text[i], end ="")
        time.sleep(float(.015))

    print("\n")


def draw_HUD():# draws the players HUD
    print("--------------------------")
    print("Stats: ")
    print(f"Player Name:   {p1.name}")
    print(f"Player Health: {p1.health}", "%")
    print(f"Player Power:  {p1.power}","%")
    print(f"Player Regen:  {p1.regen}")
    print(f"Robot health:  {r1.health}","%") # shows the robot's health
    print("--------------------------")
    print(1 * "\n")

def power_usage():
    if p1.power > 0:
        randomNumber = random.randrange(1, 13)
        if p1.power - randomNumber < 0:
            # Set power to 0 if the result of subtraction is negative
            p1.power = 0
            print(f"{p1.name} used all their remaining power. Power is now 0%.")
        else:
            # Subtract the random number from the player's power
            p1.power -= randomNumber
            print(f"{p1.name} used {randomNumber} power. Remaining power: {p1.power}%.")
            print("\n")
    elif p1.power <= 0:
        # Power is already 0, notify the player
        p1.power = 0
        print("You have no more power!!!")

def attack_Robot():#this method is the one that is used to attack the robot
    play_sound_effect(hitEffect_music)
    if p1.power >= 75:
        randomNumber = random.randrange(1,20)  # In theory, I don't even need to keep reprogramming this BUT
        # I need different RNG simply because they serve different purposes
        r1.health = r1.health - randomNumber# basic calc to get the difference
        print(p1.name, " has done", randomNumber, " damage..")
        print("Ouch...")  # ouch
        time.sleep(1)
    elif p1.power < 75 and p1.power >= 50:
        randomNumber = random.randrange(1,15)
        r1.health = r1.health - randomNumber
        print(p1.name, " has done", randomNumber, " damage..")
        print("Ouch...")  # ouch
        time.sleep(1)
    elif p1.power < 50 and p1.power >= 25:
        randomNumber = random.randrange(1, 12)
        r1.health = r1.health - randomNumber
        print(p1.name, " has done", randomNumber, " damage..")
        print("Ouch...")  # ouch
        time.sleep(1)
    elif p1.power < 25 and p1.power >= 5:
        randomNumber = random.randrange(1, 10)
        r1.health = r1.health - randomNumber
        print(p1.name, " has done", randomNumber, " damage..")
        print("Ouch...")  # ouch
        time.sleep(1)
    elif p1.power < 5 and p1.power >= 0:
        randomNumber = random.randrange(0, 5)
        r1.health = r1.health - randomNumber
        print(p1.name, " has done", randomNumber, " damage..")
        print("Ouch...")  # ouch
        time.sleep(1)


def Robot_ReturnAttack():#this allows the robot to attack after the player. the robot CAN do 0 damage :):
    randomNumber = random.randrange(0, 10)
    if randomNumber == 0:
        print("The Robot has missed!!!")
    else:# if that number is not 0 then it runs this block of code
        print("\n","The robot has gone on the attack!!! ...... ")
        play_sound_effect(laser_sfx)
        p1.health = p1.health - randomNumber
        time.sleep(.5)
        print("\n")
        print(f"The robot has done... {randomNumber} damage..")
        time.sleep(2)
        print("\n")


def player_Regen():# If the player types "Regen", it will regen the players health from an amount between the minimum and the maximum:
    if p1.regen > 0 and p1.health <= 100:
        p1.regen = p1.regen - 1
        randomNumber = random.randrange(1, 10)
        play_sound_effect(powerup_sfx)
        p1.health = p1.health + randomNumber
        print(f"The Player has gained {randomNumber} Amount of health!!!")
    else:
        print("You cannot regen!!!")


def game_overChecker(): # constantly checks if the player has reached 0health
    if p1.health <= 0:
        print(100*"\n")
        print("Game over.... you died")
        time.sleep(5)
        variable_reset()  # if the player wins or dies and wants to try again then it resets the variables
        background_music.stop()
        main_gameLoop() # if so, the game will restart
    elif r1.health <= 0:
        play_sound_effect(defeat_sound)
        print(100 * "\n")
        print("You win!!!")
        end_message()
        end_message2()

        time.sleep(5)
        variable_reset()  # if the player wins or dies and wants to try again then it resets the variables
        background_music.stop()
        main_gameLoop()



def main_gameLoop():#maimloop
    answer1 = input("Are you ready?: ")
    if answer1 == "y" or answer1 == "yes" or  answer1 == "Yes" or answer1 == "YES":
        background_music.play(-1)
        title_screen()


        p1.name = input("Please enter your name : " )
        time.sleep(.5)
        draw_robot(array)
        time.sleep(.5)
        while gameLoop == True:
            draw_HUD()
            game_overChecker()
            playerChoice = input("What is your next move? Attack|Regen| : ")
            if playerChoice == "Attack" or  playerChoice == "A" or playerChoice == "a":
                power_usage()
                attack_Robot()
                Robot_ReturnAttack()
            if playerChoice == "Regen" or  playerChoice == "R" or playerChoice == "r":
                player_Regen()
            else:
                print()

    else:
        print("Goodbye!!")
        sys.exit()

main_gameLoop()