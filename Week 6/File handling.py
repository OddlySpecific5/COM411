import os
import time as t

def cwd():
    path = os.path.realpath(__file__)
    print(f"Current working directory: {path}")

    for file in os.listdir(r"C:\Users\0mcmac68\PycharmProjects\COM411\Week 6"):
        print(f"Files in the folder: {file}")


def run():
    print("Processing...")
    t.sleep(.5)
    cwd()

def display_chars(file_path, numOfLetter):
    with open(file_path) as f:
        print(f.read(numOfLetter).strip())


def display_line(file_path):
    with open(file_path) as f:
        print(f.readline().strip())

def display_text(file_path):
    with open(file_path) as f:
        print(f.read().strip())

def run_task2():
    print("DisplayText: " , end ="")
    display_text(r"C:\Users\0mcmac68\PycharmProjects\COM411\files\library")
    print()
    print("DisplayLine: ", end="")
    display_line(r"C:\Users\0mcmac68\PycharmProjects\COM411\files\library")
    print()
    print("DisplayChars: ", end="")
    display_chars(r"C:\Users\0mcmac68\PycharmProjects\COM411\files\library", 10)


def search(filePath):
    with open(filePath) as f:
        for line in f:
            print(f"Searching in {line}".strip())
        print("Done!!!")

def run_task3():
    filePath = r"C:\Users\0mcmac68\PycharmProjects\COM411\files\library"
    search(filePath)

def search_books(filePath):
    print("Searching...")
    sections = ""
    books = "Books:\n"
    with open(filePath) as f:
        for line in f:
            if line.startswith("Section"):
                sections += line
            else:
                books += line

    print("Done")

    return f"{sections}\n\n{books}"



if __name__ == "__main__":
    question = input("What program do you want? : ")
    if question == "1":
        run()
    elif question == "2":
        run_task2()
    elif question == "3":
        book = input("What book do you want?? : ")
        run_task3()
    elif question == "4":
        search_books(r"C:\Users\0mcmac68\PycharmProjects\COM411\files\books")



