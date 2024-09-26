import os
import sys
import time

from docutils.io import Input
from pyloco import system
from virtualenv.discovery.cached_py_info import clear

array = [["#","#","#","#","#","#","#","#","#","#"],
        ["#","O"," "," "," "," "," "," ","O","#"],
        ["#"," "," "," "," "," "," "," "," ","#"],
        ["#","#","#","-","-","-","-","-","#","#"]]

hearts = "♥♥♥"
powerLevel = 99


def draw_robot(array):
    for i in range(0, 4):
        for j in range(1, 2):
            print(array[i])

def drawHUD():
        print("Hearts: " + hearts)
        print("Powerlevel: ","\n",  powerLevel)


answer1 = input("Are you ready?: ")

if answer1 == "y":
        time.sleep(.5)
        draw_robot(array)
        time.sleep(1.5)
        drawHUD()
        input("What is your next move? : ")
else:
        sys.exit()


