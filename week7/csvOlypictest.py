import csv
from sys import intern

tallyMedals = {"Gold": 0, "Silver": 0, "Bronze": 0}


def started(msg=""):
    print("-------------------------------------------------------------------------------------")#Got ChatGPT to output 85 dashes. I am not doing all of that >:(
    print(f"Operation started: {msg}")


def error(msg):
    print(f"Error! {msg}")


def completed():
    print()
    print("Operation completed")
    print("-------------------------------------------------------------------------------------")


def menu():
    print()
    print("Please select one of the following options: ")
    print(f"[years] List unique years \n" 
         f"[tally] Tally up medals \n"
         f"[teams] Tally up medals for each team \n" #Changed "tally" to "team"
        f"[country] Search for a specific team \n"
         f"[exit] Exit the program")



def display_medal_tally(tally):
    with open(r"C:\Users\Cole\PycharmProjects\COM411\week7\athlete_events.csv") as OlypTextFile:
        FileReader = csv.reader(OlypTextFile)
        for line in FileReader:
            medalAwarded = line[14] # this functions works by searching through the index:14th column and updates the respective values
            if medalAwarded == "Gold":
                tallyMedals["Gold"] += 1
            elif medalAwarded == "Silver":
                tallyMedals["Silver"] += 1
            elif medalAwarded == "Bronze":
                tallyMedals["Bronze"] += 1

    print()
    print("|Gold     |"f"{tallyMedals["Gold"]}|")
    print("|Silver   |"f"{tallyMedals["Silver"]}|")
    print("|Bronze   |"f"{tallyMedals["Bronze"]}|")




def display_medal_tallyTeam(team_tally):
    #Had a eureka  moment and made this gem
    countryList = []# Dup checker
    listOfTeams = [] # This was made prior to knowing sets and, I'm too lazy to change it
    with open(r"athlete_events.csv") as OlypTextFile:
        FileReader = csv.reader(OlypTextFile)
        next(FileReader) #  Skips the header
        for line in FileReader:
            country = line[6]
            medalAwarded = line[14]
            if country not in countryList: # if the country is NOT in the country list
                countryList.append(country)# adds the respective country to the list
                countryDictionary = {"Country": country, "Medals":{"Gold": 0, "Silver": 0, "Bronze": 0}}
                listOfTeams.append(countryDictionary) # creates and appends
                # s the country to the list, via dictionary
            else:
                countryDictionary = next(team for team in listOfTeams if team["Country"] == country) # used ChatGPT for this line because I am fairly shit at dictionaries

            if medalAwarded in countryDictionary["Medals"]: #searchs through the dictionary and increments the medals
                countryDictionary["Medals"][medalAwarded] += 1

        for countryDictionary in listOfTeams: # Assuming everything is correct, this should print everything out with no issue
            print("-------------------------------------------------------------------------------------")
            print(countryDictionary["Country"])

            print("|Gold     |"f"{countryDictionary["Medals"]["Gold"]}|")
            print("|Silver   |"f"{countryDictionary["Medals"]["Silver"]}|")
            print("|Bronze   |"f"{countryDictionary["Medals"]["Bronze"]}|")
            print("-------------------------------------------------------------------------------------")


def display_specifc_country(countryName):
    countryDictionary = {"Country": countryName, "Medals": {"Gold": 0, "Silver": 0, "Bronze": 0}}
    countryFound = False
    listOfTeams = []
    with open(r"athlete_events.csv") as OlypTextFile:
        FileReader = csv.reader(OlypTextFile)
        next(FileReader)  # Skips the header
        for line in FileReader:
            country = line[6]
            medalAwarded = line[14]
            if country == countryName:  # if the country is NOT in the country list
                countryFound = True
                if medalAwarded in countryDictionary["Medals"]:  # searchs through the dictionary and increments the medals
                    countryDictionary["Medals"][medalAwarded] += 1


        if countryFound:
            print("-------------------")
            print(countryDictionary["Country"])
            print("|Gold     |", countryDictionary["Medals"]["Gold"], "|")
            print("|Silver   |", countryDictionary["Medals"]["Silver"], "|")
            print("|Bronze   |", countryDictionary["Medals"]["Bronze"], "|")
            print("-------------------")
        else:
            print(f"{countryName}' is not in the database.")



def display_years(years):
    print("Years here!!!")
    with open(r"athlete_events.csv") as OlypTextFile:
        FileReader = csv.reader(OlypTextFile)
        print(f"Years: ")
        listOyears = []
        print("-------------------")
        for line in FileReader:
            listOyears.append(line[9])# adds every read year to a list
            print(line[9])
            print("-------------------")
    #The purpose / desired outcome WASN'T to add it to a list but I did it  because it would make it easier to manipulate.
    # Attempting to sort via "Sort()" will take too long, this is assuming it runs a basic bubble sort and a much stronger sorting algorithm (Insertion / Quick sort for intergers) will be needed
