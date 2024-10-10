import time

def program_1():
    appleNum = int(input("How many apples do you want: "))
    count = 1
    while count <= appleNum:
        print(f"Removed {count}  of apples ")
        count += 1


def program_2():
    robotQuestion = int(input("How many obstecules do you want me to avoid:  "))
    track = 0
    while track != robotQuestion:
        track += 1
        print("Avoiding....")
        print(f"Avoided {track} Obsticules!!")
        time.sleep(.5)
    print("\n")
    print(f"Avoided {track} Obsticules in total..!!!!")


def program_3():


while True:#mainloop
    print(2 * "\n")
    question1 = int(input("What program do you want?: "))
    if question1 == 1:
        program_1()
    elif question1 == 2:
        program_2()
    elif question1 == 3:
        program_3()


