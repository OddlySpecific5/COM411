import time


def program1():
    bookType = input("What genre is your book? :  ").lower()

    if bookType == "adventure":  # if the user puts "adventure" into the book genre
        print(f"I like {bookType}!!!")

    elif bookType == "science":  # same code, just with Science!
        print(f"I like {bookType} books!!!")

    bookName = input("What is the name of your book? :  ")  # asks the user for the name of their book
    print(f"I love {bookName} ! That one is my favourite")  # prints out the name of their book



def program2():
    activityChoice = input("What activity do you want to do? : ").lower()
    if activityChoice == "calculate":
        time.sleep(.5)
        print("\n")
        print("doing calculations...")
        time.sleep(.5)
        print("Activity complete!!")
        program2()


    else:
        print("Performing activity")
        time.sleep(.5)
        print("Activity complete!!")
        program2()


program2()