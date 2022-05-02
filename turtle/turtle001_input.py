'''
Exploring Python turtle
Lucas, Berat, Julian
25.04.2022
'''

#importing classes
from random import *
from turtle import *
#
# Functions
#

# Draws a square
def square(size):
    for i in range(4):
        forward(size)
        left(90)

# Draws a rectangle
def rectangle(a, b):
    for i in range(2):
        forward(a)
        left(90)
        forward(b)
        left(90)

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

# Draws the House at given coords with given colors
def house(startx, starty, pencolor, fillcolor, scale):
    move(startx, starty)
    colorchange(pencolor, fillcolor)

    speed(1000)
    square(100*scale)

    move(xcor() + 100*scale, ycor() + 100*scale)
    left(135)
    forward(70.711*scale)
    left(90)
    forward(70.711*scale)

    colorchange(pencolor, '#00fcf0')
    move(xcor() + 15*scale, ycor() - 30*scale)
    square(20*scale)

    colorchange(pencolor, '#00fcf0')
    move(xcor() + 50*scale, ycor())
    square(20*scale)

    colorchange(pencolor, '#593323')
    move(xcor() - 15*scale, ycor() - 70*scale)
    rectangle(20*scale, 40*scale)

    colorchange('#fffb00', '#fffb00')
    move(xcor() + 3*scale, ycor() + 15*scale)
    circle(2.5*scale)

    end_fill()


while True:
    for x in range(30):
        print(" ")
    print("██╗  ██╗ █████╗ ██╗   ██╗███████╗ ██████╗ ███████╗███╗   ██╗███████╗██████╗  █████╗ ████████╗ ██████╗ ██████╗ ")
    print("██║  ██║██╔══██╗██║   ██║██╔════╝██╔════╝ ██╔════╝████╗  ██║██╔════╝██╔══██╗██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗")
    print("███████║███████║██║   ██║███████╗██║  ███╗█████╗  ██╔██╗ ██║█████╗  ██████╔╝███████║   ██║   ██║   ██║██████╔╝")
    print("██╔══██║██╔══██║██║   ██║╚════██║██║   ██║██╔══╝  ██║╚██╗██║██╔══╝  ██╔══██╗██╔══██║   ██║   ██║   ██║██╔══██╗")
    print("██║  ██║██║  ██║╚██████╔╝███████║╚██████╔╝███████╗██║ ╚████║███████╗██║  ██║██║  ██║   ██║   ╚██████╔╝██║  ██║")
    print("╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝ ╚═════╝ ╚══════╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝")
    pen = input("Gib einen Hex code für die Farbe der Outline ein (end für abbruch): ")
    if(pen == "end"):
        break
    back = input("Gib einen Hex code für die Hausfarbe ein: ")
    ranX = float(input("Gib die Start-X-Koordinate ein: "))
    ranY = float(input("Gib die Start-Y-Koordinate ein: "))
    scale = float(input("Gib die Größe des Hauses ein (0.5 - Halb so groß; 2 - Doppelt so groß): "))
    house(ranX, ranY, pen, back, scale)