import time as t
from operator import concat

# Navi ahh
def user_listen():
    userResponse = input("What do you hear?: ")
    full = " That was a loud noise!! .... I just heard a "
    newString = concat(full, userResponse)
    print("You: ", end="")
    for i in range(0, len(newString)):
        print(newString[i], end="")
        t.sleep(float(0.21))
# Why?



def user_identify():
    textSpeed = float(0.19)
    userResponse = input("What do you see?: ")
    if userResponse == "boulder":
        full = " i see a "
        newString = concat(full, userResponse)
        print("You: ", end="")
        for i in range(0, len(newString)):
            print(newString[i], end="")
            t.sleep(textSpeed)

        print("\n")
        friendText = "We need to run!!!"
        print("Friend: ", end="")
        for i in range(0, len(friendText)):
            print(friendText[i], end="")
            t.sleep(textSpeed)




    else:
        full = " i see a "
        newString = concat(full, userResponse)
        print("You: ", end="")
        for i in range(0, len(newString)):
            print(newString[i], end="")
            t.sleep(float(0.21))
        print("\n","Friend: We'll be fine..")


while True:
    print("\n")
    userChoice = input("What do you do?: ").lower()
    if userChoice == "listen":
        user_listen()
    elif userChoice == "identify":
        user_identify()
