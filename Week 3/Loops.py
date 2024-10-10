import time
from typing import Counter

from pygame.midi import Input


def program_1():
    appleNum = int(input("How many apples do you want: "))
    count = 1
    while count <= appleNum:
        print(f"Removed {count}  of apples ")
        count += 1


def program_2():
    robotQuestion = int(input("How many obstecules do you want me to avoid:  "))
    track = 0
    while track != robotQuestion:
        track += 1
        print("Avoiding....")
        print(f"Avoided {track} Obsticules!!")
        time.sleep(.5)
    print("\n")
    print(f"Avoided {track} Obsticules in total..!!!!")


def program_3():
    robotCharge = int(input("How much do you want to charge the robot's battery by?:  "))
    i = 1

    while i < robotCharge:
        print(f"Charge: {'█'*i}")
        i +=1

def program_4():
    userResponse = input("Please enter a phrase: ")
    for i in range (0,len(userResponse)):
       print("Hi", end=" ")



def program_5():
    counter1 = 0
    counter2 = 1
    while counter2 <= 100:
        counter1 = counter1 + counter2
        counter2 += 1

        print(f"Sum of 1 to 100: {counter1}")

    print("\n")
    print(f"Total sum is {counter1}")


def program_6():
    userChoice = int(input("How many numbers should I sum up?: "))
    count = 1
    TempVar = 0
    while count <= userChoice:
        main_number = int(input(f"Please enter a number {count} out of {userChoice}: "))
        TempVar = TempVar + main_number

        count += 1
    print(f"Final sum of the numbers {TempVar}")


while True:#mainloop
    print(2 * "\n")
    question1 = int(input("What program do you want?: "))
    if question1 == 1:
        program_1()
    elif question1 == 2:
        program_2()
    elif question1 == 3:
        program_3()
    elif question1 == 4:
        program_4()
    elif question1 == 5:
        program_5()
    elif question1 == 6:
        program_6()
    elif question1 == 7:
        program_7()

