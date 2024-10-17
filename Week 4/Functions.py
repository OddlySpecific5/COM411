import sys


def program1():
    print("Program Started!")
    userInput = input("Enter a character: ")
    print(f"The Ascii of your character is {ord(userInput)}")




while True:  # mainloop
    print(2 * "\n")
    question1 = int(input("What program do you want?: "))
    if question1 == 1:
        program1()
    else:
        sys.exit()
