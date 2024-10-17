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



def escape_by(method):
    if method == "jumping over":
        print(f"{method} :  We cannot escape that way! The boulder is too big")
    elif method == "running around":
        print(f"{method} :We cannot escape that way! The boulder is moving too fast!")
    elif method == "cross bridge ahead":
        print(f"{method} :That might just work! Let's go!")
    else:
        print(f"{method} :That is not an option!!")


def cross_bridgefunc(steps):
    for i in range(1, steps + 1):
        print(f"Crossed step")
    if i > 5:
        print("The bridge is falling down!!!!")
    else:
        print("We must keep going!!!")



while True:
    print("\n")
    userChoice = input("What do you do?: ").lower()
    if userChoice == "listen":
        user_listen()
    elif userChoice == "identify":
        user_identify()
    elif userChoice == "escape":
        escape_by("jumping over")
        escape_by("running around")
        escape_by("cross bridge ahead")
        escape_by("jumping till we fly!!!")
    elif userChoice == "cross":
        cross_bridgefunc(100)

