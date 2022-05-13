'''
dritte Hausübung - Themen: Zahlenrate spiel
random Zahl erstellen - user abfrage - sagen ob zahl goesser oder kleiner ist & versuche anzeigen-
user gewinnt wenn er die Zahl errät
Lucas
09.05.2022
'''
import random
import os

#greet user and taking upper limit
print("╔═══════════════╗")
print("  ZAHLENRATEN")
print("╚═══════════════╝")
print(" ")

name = input("What's your name? ")
if '|' in name:
    name = name.replace('|', ' ')

print("Wellcome {} this is a number guessing game. You set a upper limit and than you guess. Less guesses are better!".format(name))
print("Good luck, Have fun")
print(" ")
print(" ")
upperLimit = int(input("[NumberGuessing] Please set the upper limit that is greater than 1: "))
print(" ")
print(" ")

#indikating variables
tries = 1
on = True
debugMode = True
#calc random number
random = random.randint(1,upperLimit)

#game loop: get if number is bigger or smaller and tries +1
print("[NumberGuessing] (Gamemaster): Ok i will lead the game now. I got a random number between 1 and {}. You have to guess. I will give you hints if the number is greater or lower.".format(upperLimit))
if(debugMode):
    print("Number =",random)
print(" ")
while(on):
    ui = int(input("[NumberGuessing] (Gamemaster): Now guess a number: "))

    if(random == ui):
        points = int(upperLimit/tries)
        print("[NumberGuessing] (Gamemaster): You got it. The number was {}. You got it in {} Tries. You got {} points".format(random,tries,points))

        #opens file and inits highscore
        filer = open("highscores.txt", "r")
        lines = filer.read().splitlines()
        names = []
        scores = []

        #reads file and splits names and scores
        for i in lines:
            names.append(i.split("|")[0])  # split the line into a list
            scores.append(int(i.split("|")[1]))
        filer.close()

        scores, names = zip(*sorted(zip(scores, names), reverse=True))  # sort the highscores

        #converts tuples to lists
        names = list(names)
        scores = list(scores)

        #adds new highscore
        for i in range(len(names)):
            if (points > int(scores[i])):
                names.insert(i, name)
                scores.insert(i, points)
                break

        # prints highscores
        for i in range(len(names)):
            if i == 5:
                break
            print(str(i + 1) + ". " + str(names[i]) + ": " + str(scores[i]))

        # write the scoreboard to the file
        filew = open("highscores.txt", "w")
        for i in range(len(names)):
            if i == 5:
                break
            filew.write(str(names[i]) + "|" + str(scores[i]) + "\n")
        filew.close()

        break
    elif(random >= ui):
        print("[NumberGuessing] (Gamemaster): This is your {}. try and I think the number is greater than your input".format(tries))
        tries = tries +1
    elif(random <= ui):
        print("[NumberGuessing] (Gamemaster): This is your {}. try and I think the number is smaller than your input".format(tries))
        tries = tries +1