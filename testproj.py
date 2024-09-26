import sys

name = "Cole"
age = 19

counterAttemptMax = 4
clientAttempts = 0

while clientAttempts != counterAttemptMax:
    answer = input("What is your name?: ")
    if answer == "Cole":
        print("Cole")
        break
    else:
        clientAttempts += 1
        print(clientAttempts)# this adds 1 form every new attempt
        if clientAttempts == counterAttemptMax:
            print("Goodbye , you have no attempts left")
            sys.exit()
        else:
            print("Please try again :( ")

