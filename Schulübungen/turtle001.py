'''
Exploring Python turtle
Lucas, Berat, Julian
25.04.2022
'''

import random
# Import the turtle module
from turtle import *

pen = ["#"+''.join([random.choice('ABCDEF0123456789') for i in range(6)])]
back = ["#"+''.join([random.choice('ABCDEF0123456789') for i in range(6)])]

def square(length):
    '''
    Draws a square with the given length
    '''

    for i in range(4):
        forward(length)
        left(90)

def rectangle(a,b):
    '''
    Draws a rectangle with the given length
    '''
    for i in range(2):
        forward(a)
        left(90)
        forward(b)
        left(90)

def move(x,y):
    penup()
    goto(x,y)
    setheading(0)
    pendown()

def colorchange(pencolor, fillcolor):
    end_fill()
    color(pencolor, fillcolor)
    begin_fill()

def house(startx, starty, pencolor, fillcolor):
    move(startx, starty)
    colorchange(pencolor, fillcolor)

    speed(10)
    square(100)

    move(xcor() + 100, ycor() + 100)
    left(135)
    forward(70.711)
    left(90)
    forward(70.711)

    colorchange(pencolor, '#00fcf0')
    move(xcor() + 15, ycor() - 30)
    square(20)

    colorchange(pencolor, '#00fcf0')
    move(xcor() + 50, ycor())
    square(20)

    colorchange(pencolor, '#593323')
    move(xcor() - 15, ycor() - 70)
    rectangle(20, 40)

    colorchange('#fffb00', '#fffb00')
    move(xcor() + 3, ycor() + 15)
    circle(2.5)

    end_fill()

while (True):
    height = float(window_height())
    width = float(window_width())
    xcor = random.randint((width)*(-1)), (window_width()/2))
    ycor = random.randint((window_height()/2)*(-1), window_height()/2)
    house(xcor, ycor, pen, back)