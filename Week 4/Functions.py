import sys


def program1():
    print(f"Program 1 Started!")
    userInput = input("Enter a character: ")
    print(f"The Ascii of your character is {ord(userInput)}")

def program2():
    print(f"Program 2 Started!")
    userInput = int(input("Enter the Ascii code of a number: "))
    if 32 <= userInput <= 127:
        print(f" The Ascii code of your number is {userInput}, the character is {chr(userInput)}")
    else:
        print("Error")
        print("Ending Program")


def program3():
    print(f"Program 3 Started!")




while True:  # mainloop
    print(2 * "\n")
    question1 = int(input("What program do you want?: "))
    if question1 == 1:
        program1()
    elif question1 == 2:
        program2()
    else:
        sys.exit()
