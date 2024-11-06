import csv
import csvOlypictest


def read_data(file_path):
    print()

def run(file_path):
    athlete_data = read_data(file_path)
    with open(file_path) as fp:
        csvOlypictest.started()
        while True:
            selection = input("What do you want to select? : ").lower()
            if selection == "years":
                csvOlypictest.display_years(selection)  # Years won
            elif selection == "tally":
                csvOlypictest.display_medal_tally(selection)  # Regular Tally
            elif selection == "team":
                csvOlypictest.display_medal_tallyTeam(selection)  # Team Tally
            elif selection == "exit":
                break
            else:
                csvOlypictest.error(msg="Invalid selection")





run(r"C:\Users\Cole\PycharmProjects\COM411\week7\athlete_events.csv")