'''
Coding Hangman with turtle graphics
Lucas
02.05.2022
'''
from turtle import *
import random

# Config
Debug = True
prefix = "[Hangman] "

# Hangman word list
file = open("words.txt", "r")
words = file.read().splitlines()

word_to_guess = random.choice(words)
file.close()
word_split = list(word_to_guess)
char_guessed = []
word_underscores = []
losses = 0


# Moves the turtle without a line behind it
def move(x, y):
    penup()
    goto(x, y)
    setheading(0)
    pendown()


# ends fill - changes color - starts new fill
def colorchange(pencolor, fillcolor):
    end_fill()
    color(pencolor, fillcolor)
    begin_fill()


# Draws a rectangle
def rectangle(a, b):
    for i in range(2):
        forward(a)
        left(90)
        forward(b)
        left(90)


# Draws the hangman
def draw(losses):
    clearscreen()
    tracer(0)

    move(-460, 350)
    write("Wrong guesses: {}".format(losses), font=("Arial", 30, "normal"))
    if losses == 0:
        return None

    for i in range(losses+1):
        print("i=",i)

        if (i == 1):

            move(-10, -25)
            colorchange("black", "black")
            setheading(135)
            rectangle(10, 50)
            colorchange("black", "black")

        elif (i == 2):

            colorchange("black", "black")
            move(25, -60)
            colorchange("black", "black")
            setheading(45)
            rectangle(10, 50)
            colorchange("black", "black")

        elif (i == 3):

            move(-15, -25)
            colorchange("black", "black")
            setheading(0)
            rectangle(10, 100)
            colorchange("black", "black")

        elif (i == 4):

            move(-15, 75)
            colorchange("black", "black")
            setheading(270)
            rectangle(10, 75)
            colorchange("black", "black")

        elif (i == 5):

            move(60, 75)
            colorchange("black", "black")
            setheading(180)
            rectangle(10, 30)
            colorchange("black", "black")

        elif (i == 6):

            move(55, 50)
            colorchange("black", "black")
            setheading(180)
            circle(17)

            move(55, 17)
            setheading(270)
            forward(37)

            right(45)
            forward(20)

            move(55, -20)
            right(45)
            forward(20)

            move(55, 0)
            left(45)
            forward(20)
            move(55, 0)
            right(225)
            forward(20)
    update()

def show_word():
    erg = ""  # displays the word in a good format
    erg2 = ""  # displays the guessed letters in a good format

    char_guessed.sort()  # sorts the list of guessed letters (alphabetically a,b,c,...,z)

    # formats the word
    for x in word_underscores:
        erg = erg + x

    # formats the guessed letters
    for i in char_guessed:
        erg2 = erg2 + " " + i

    for i in range(20):
        print("")

    print("")
    print("██╗  ██╗ █████╗ ███╗   ██╗ ██████╗ ███╗   ███╗ █████╗ ███╗   ██╗")
    print("██║  ██║██╔══██╗████╗  ██║██╔════╝ ████╗ ████║██╔══██╗████╗  ██║")
    print("███████║███████║██╔██╗ ██║██║  ███╗██╔████╔██║███████║██╔██╗ ██║")
    print("██╔══██║██╔══██║██║╚██╗██║██║   ██║██║╚██╔╝██║██╔══██║██║╚██╗██║")
    print("██║  ██║██║  ██║██║ ╚████║╚██████╔╝██║ ╚═╝ ██║██║  ██║██║ ╚████║")
    print("╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝")
    print("")
    print(prefix,"You guessed following letters: \n " + erg2 + "\n")
    print(prefix,"The word is: ", erg)


# getting the word and turning it into list
for i in range(len(word_to_guess)):
    word_underscores.append("_")

while (True):

    show_word()

    guess = input(prefix + "Please enter one letter you want to guess: ")

    # checks if the guess is a letter
    if (len(guess) == 1 and guess.isalpha()):
        guess = guess.lower()
        # adding guess to list of guessed letters (if not there already)
        if (guess in char_guessed):
            print(prefix,"You have already guessed that letter!")
            continue
        else:
            char_guessed.append(guess)

        # checking if the guess is in the word (if yes then the underscore is replaced)
        in_word = False
        for i in range(len(word_to_guess)):
            if (word_to_guess[i] == guess):
                in_word = True
                word_underscores[i] = guess

        # if the guess is not in the word then the hangman is drawn (losses +1)
        # if the losses are 6 then the game is over
        if (in_word == False):

            losses += 1
            draw(losses)

            if losses == 6:
                print(prefix,"You lost! The word was: " + word_to_guess)
                break

        # if the word is guessed then the game is over
        if (word_underscores == word_split):
            print(prefix,"You won! Congrats! The word was: " + word_to_guess)
            break

    else:
        print(prefix,"Please enter a letter!")
        continue
