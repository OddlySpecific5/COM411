import csv
import csvOlypictest


def read_data(file_path):
    print(f"Reading data from {file_path}")

def run(file_path):
    with open(file_path) as fp:
        while True:
            csvOlypictest.menu()
            print()
            selection = input("What do you want to select? : ").lower()
            if selection == "years":# Allows the user to see the years
                csvOlypictest.started(f"Listing {selection}")
                read_data(file_path)
                csvOlypictest.display_years(selection)  #display_years()
                csvOlypictest.completed()
            elif selection == "tally":# Allows the user to see the total tally of years worth of awards won
                csvOlypictest.started(f"Tallying medals")
                read_data(file_path)
                csvOlypictest.display_medal_tally(selection) #display_medal_tally()
                csvOlypictest.completed()
            elif selection == "teams":# Allows the user to see the total amount of awards won by each team
                csvOlypictest.started("Tallying medals for each team.")
                read_data(file_path)
                csvOlypictest.display_medal_tallyTeam(selection)  #display_medal_tallyTeam()
                csvOlypictest.completed()
            elif selection == "country":# Allows the user to see the total amount of awards won by each team specifically chosen by the user
                countryName = input("What country do you want to search for?: ")
                csvOlypictest.started(f"Tallying the medals for {countryName}")
                csvOlypictest.display_specifc_country(countryName)
                csvOlypictest.completed()
            elif selection == "exit":
                csvOlypictest.completed()
                break
            else:
                csvOlypictest.error(msg="Invalid selection")
















run(r"C:\Users\Cole\PycharmProjects\COM411\week7\athlete_events.csv")