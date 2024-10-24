from tempfile import tempdir


def directions():
    steps = ["Move Forward", "Move Backward", "Turn Left", "Turn Right"]
    return steps


def run_1():
    print(directions())




def movements():
    path = ["MoveForward", 10, "Move Backward", 5, "Move Left", 3, "Move Right", 1]
    return path

def run_2():
    print("Moving....")
    temp = movements()
    for i in range(0, len(temp) , 2):
        print(f"{temp[i]} to {temp[i+1]}")



def menu():
    tempDirections = directions()
    for i in range(0, len(tempDirections)):
        print(f"{i} : {tempDirections[i]}")
    directionChoice = input("Which direction would you like to move?: " )



def run_4():
    routeList = []

    for i in range(1, 6):
        routeList.append(menu_and_input())

    for i in range(0, len(routeList)):
        print(f"Escape route: {i + 1} : {routeList[i]}")

    print("\n" + f"In a list format, here is your escape route:  {routeList}")



def menu_and_input():
    localTemp = directions() # displays diirections
    for i in range(0, len(localTemp)):
        print(f"{i} : {localTemp[i]}")

    while True:
        playerChoice = int(input("Which route would you like to move to??: "))
        if playerChoice >= len(localTemp):
            print()
        else:
            return localTemp[playerChoice]
            break





def run_3():
    menu()





if __name__ == "__main__":
    question = input("What program do you want? : ")
    if question == "1":
        run_1()
    elif question == "2":
        run_2()
    elif question == "3":
        run_3()
    elif question == "4":
        run_4()