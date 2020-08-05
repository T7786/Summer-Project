import os
import datetime
import re
from dataclasses import dataclass
from datetime import date

@dataclass
class Game:
    Name: str
    Date: datetime
    Description: str
    Scores: list


def main():
    Games_dir = "C:/Users/Taran/PycharmProjects/untitled/Games"
    for filename in os.listdir(Games_dir):
        file = open(Games_dir + "/" + filename, errors='ignore')

        name = ""
        date = datetime
        description = ""
        scores = []
        for line in file:

            tokens = line.strip().split(":")
            if tokens[0] == "Game Name":
                name = tokens[1]

            elif tokens[0] == "Release Date":
                date = tokens[1]

            elif tokens[0] == "Description":
                description = tokens[1]

    running = True

    while running:
        line = input(">> ")
        tokens = line.strip().split(" ")
        cmd = tokens[0]

        if cmd == "help":
            print("\thelp - print this message\n",
                  "\tlist - show available archived games\n",
                  "\tprint(GameName) - prints the file on selected game\n",
                  "\tdate(GameName) - prints the date on selected game\n",
                  "\tprint(GameName) - prints the file on selected game\n",
                  "\tquit - stops the program")
        elif cmd == "quit":
            print("quitting...")
            running = False
        elif cmd == "list":
            print("RocketLeague.txt")
        elif cmd == "print(RocketLeague)":
            file = open("Games/RocketLeague.txt")  # opens the file with info on the game
            x = file.readline()  # skips the first line that just says "grades:"
            print(x)
            x = file.readline()  # skips the first line that just says "grades:"
            print(x)
            x = file.readline()  # skips the first line that just says "grades:"
            print(x)
            x = file.readline()  # skips the first line that just says "grades:"
            print(x)
            x = file.readline()  # skips the first line that just says "grades:"
            print(x)
            x = file.readline()  # skips the first line that just says "grades:"
            print(x)
            x = file.readline()  # skips the first line that just says "grades:"
            print(x)
            x = file.readline()  # skips the first line that just says "grades:"
            print(x)
        elif cmd == "date(RocketLeague)":
            file = open("Games/RocketLeague.txt")  # opens the file with info on the game
            file.readline()  # skips the first line that just says "grades:"
            s = file.readline()
            print(s)
            match = re.search(r'\d{2}-\d{2}-\d{4}', s)
            date = datetime.datetime.strptime(match.group(), '%d-%m-%Y').date()
            print(date)

        else:
            print("Not a recognized command, try typing 'help'")

    directory = "C:/Users/Taran/PycharmProjects/untitled"

    for filename in os.listdir(directory):
        print(filename)


if __name__ == '__main__':
    main()
