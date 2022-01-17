'''
dritte Hausübung - Themen: Zahlenrate spiel
random Zahl erstellen - user abfrage - sagen ob zahl goesser oder kleiner ist & versuche anzeigen-
user gewinnt wenn er die Zahl errät
Lucas
17.01.2022
'''
import random
import getpass
#greet user and taking upper limit
print("╔═══════════════╗")
print("  ZAHLENRATEN")
print("╚═══════════════╝")
print(" ")
print("Wellcome {} this is a number guessing game. You set a upper limit and than you guess. Less guesses are better!".format(getpass.getuser()))
print("Good luck, Have fun")
print(" ")
print(" ")
upperLimit = int(input("[NumberGuessing] Please set the upper limit that is greater than 1: "))
print(" ")
print(" ")
#indikating variables
tries = 0
on = True
#calc random number
random = random.randint(1,upperLimit)

#game loop: get if number is bigger or smaller and tries +1
print("[NumberGuessing] (Gamemaster): Ok i will lead the game now. I got a random number between 1 and {}. You have to guess. I will give you hints if the number is greater or lower.".format(upperLimit))
print(" ")
while(on):
    ui = int(input("[NumberGuessing] (Gamemaster): Now guess a number: "))
    if(random == ui):
        print("[NumberGuessing] (Gamemaster): You got it. The number was {}. You got it in {} Tries".format(random,tries))
        file.
        break
    elif(random >= ui):
        print("[NumberGuessing] (Gamemaster): The number I think of is greater than your input")
        tries = tries +1
    elif(random <= ui):
        print("[NumberGuessing] (Gamemaster): The number I think of is smaller than your input")
        tries = tries +1