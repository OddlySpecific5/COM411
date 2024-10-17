import time as t
from operator import concat


def listen():
    userResponse = input("What do you hear?: ")
    full = " That was a loud!! .... I just heard a "
    newString = concat(full, userResponse)
    print("You: ", end="")
    for i in range(0, len(newString)):
        print(newString[i], end="")
        t.sleep(float(0.21))
# Why? because im an extra immmanuel Kant!!

listen()
