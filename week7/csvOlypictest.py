import csv
import process
import tui

def started(msg=""):
    print("-------------------------------------------------------------------------------------")#Got ChatGPT to output 85 dashes. I am not doing all of that >:(
    print(f"Operation started: {msg}")


def error(msg):
    print(f"Error! {msg}")


def completed():
    print(("Operation completed"))
    print("-------------------------------------------------------------------------------------")




def menu():
    print(f"[years] List unique years \n" 
         f"[tally] Tally up medals \n"
         f"[ctally] Tally up medals for each team \n"
         f"[exit] Exit the program")



def display_medal_tally(tally):
    print()


def display_medal_tally(team_tally):
    print()


def display_years(years):
    print()


with open(r"C:\Users\Cole\PycharmProjects\COM411\week7\athlete_events.csv", 'r') as OlypicFile:
   print()