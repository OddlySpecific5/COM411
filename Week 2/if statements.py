import time


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





program1()
program2()


