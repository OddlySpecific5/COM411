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
        print(f"Moving {temp[i]} to {temp[i+1]}")





if __name__ == "__main__":
    question = input("What program do you want? : ")
    if question == "1":
        run_1()
    elif question == "2":
        run_2()

