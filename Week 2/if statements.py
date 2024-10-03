import time

player = "x"


map = [["#","#","#","#","#","#","#","#","#","#"          ],
        ["#",player," "," "," "," "," "," "," ","#"      ],
        ["#"," "," "," "," "," "," "," "," ","#"         ],
        ["#"," "," "," "," "," "," "," "," ","#"         ],
        ["#", " ", " ", " ", " ", " ", " ", " ", " ", "#"],
        ["#", " ", " ", " ", " ", " ", " ", " ", " ", "#"],
        ["#", " ", " ", " ", " ", " ", " ", " ", "♥", "#"],
        ["#","#","#","#","#","#","#","#","#","#"]        ]

playerPosY = 1
playerPosX = 1



def program1():
    bookType = input("What genre is your book? :  ").lower()

    if bookType == "adventure":  # if the user puts "adventure" into the book genre
        print(f"I like {bookType}!!!")

    elif bookType == "science":  # same code, just with Science!
        print(f"I like {bookType} books!!!")
    else:
        print(f"Sorry we do not have {bookType.capitalize()} in store today...")# .capitalize  makes the first letter of the variable a capital
    bookName = input("What is the name of your book? :  ")  # asks the user for the name of their book
    print(f"I love {bookName} ! That one is my favourite")  # prints out the name of their book



def program2():
    while True:
        activityChoice = input(
            "What activity do you want to do? : ").lower()  # this asks the user what their prefered choice is
        if activityChoice == "calculate":  # if the user puts "calculate" then
            time.sleep(.5)  # it runs this section of code
            print("\n")
            print("doing calculations...")
            time.sleep(.5)
            print("Activity complete!!")

        else:  # if anything BUT calculate is added, it runs this
            print("Performing activity")
            time.sleep(.5)
            print("Activity complete!!")

def drawMap(map):
    for i in range(0, 8):
          for j in range(1, 2):
              print(map[i])


def Up_movement(map, playerPosY, playerPosX, player):
    map[playerPosY - 1][playerPosX] = player
    map[playerPosY][playerPosX] = ' '


def Down_movement(map, playerPosY, playerPosX, player):
    map[playerPosY + 1][playerPosX] = player
    map[playerPosY][playerPosX] = ' '




def Left_movement(map, playerPosY, playerPosX, player):
    map[playerPosY][playerPosX - 1] = player
    map[playerPosY][playerPosX] = ' '


def Right_movement(map, playerPosY, playerPosX, player):
    map[playerPosY][playerPosX + 1] = player
    map[playerPosY][playerPosX] = ' '


def program3(map, playerPosY, playerPosX, player):
    while True:
        drawMap(map)
        moveChoice = input("What way should the robot move? : Up | Down | Left| Right:  ").lower()
        if moveChoice == "up" and playerPosY != 1:
            print(f"Going {moveChoice.capitalize()} !!!! ")
            Up_movement(map, playerPosY, playerPosX, player)
            playerPosY -= 1
        elif moveChoice == "down" and playerPosY != 6:
            print(f"Going {moveChoice.capitalize()} !!!! ")
            Down_movement(map, playerPosY, playerPosX, player)
            playerPosY +=1
        elif moveChoice == "left" and playerPosX != 1:
            print(f"Going {moveChoice.capitalize()} !!!! ")
            Left_movement(map, playerPosY, playerPosX, player)
            playerPosX -=1
        elif moveChoice == "right" and playerPosX != 13:
            print(f"Going {moveChoice.capitalize()} !!!! ")
            Right_movement(map, playerPosY, playerPosX, player)
            playerPosX +=1
        else:
            print("Invalid move")





program3(map, playerPosY, playerPosX, player)


