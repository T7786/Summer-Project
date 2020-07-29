import os
import datetime
import re
from datetime import date

def main():
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
             print("RocketLeague")
        elif cmd == "print(RocketLeague)":
         file = open("RocketLeague.txt")  # opens the file with info on the game
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
         file = open("RocketLeague.txt")  # opens the file with info on the game
         file.readline()  # skips the first line that just says "grades:"
         s = file.readline()
         print(s)
         match = re.search(r'\d{2}-\d{2}-\d{4}', s)
         date = datetime.datetime.strptime(match.group(), '%d-%m-%Y').date()
         print(date)

        else:
            print("Not a recognized command, try typing 'help'")

    directory = "C:/Users/Taran/PycharmProjects/Week3/venv"

    for filename in os.listdir(directory):
        print(filename)

if __name__ == '__main__':
        main()


    #file = open("RocketLeage.txt")  # opens the file with info on the game
    #file.readline()  # skips the first line that just says "grades:"


    #directory = "C:/Users/"

#for filename in os.listdir(directory):
    #file = open(filename)