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



run()