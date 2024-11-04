import random
import time as t

count = 0


def gun():
    print(r"""
(                                 _
 )                               /=>
(  +____________________/\/\___ / /|
 .''._____________'._____      / /|/\
: () :              :\ ----\|    \ )
'..'______________.'0|----|      \
                0_0/____/        \
                    |----    /----\
                   || -\\ --|      \
                   ||   || ||\      \
                    \\____// '|      \
Bang! Bang!                 .'/       |
                           .:/        |
                           :/_________|
                                       DeXteR/MJP
""")


def game_decision():
    newValue = random.randint(0, 7)
    return newValue


print("Welcome to Russian Roulette :))) ")
while True:

    shoot = input("Do you want to shoot?: ").lower()
    if shoot == "yes" or "y":
        count += 1
        print("Shooting....")
        t.sleep(1.5)
        newNum = random.randint(0, 7)
        if newNum != game_decision():
            print("You lived another day")
        else:
            print("You died....")
            gun()
            print(f"You lived for {count} dry shots....")
            break
    else:
        print("You cannot escape...")

