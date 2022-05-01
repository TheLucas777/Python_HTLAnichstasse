'''
Same as turtle001.py but less lines
Lucas, Berat, Julian
25.04.2022
'''
from random import *
from turtle import *
def rectangle(a, b):
    for i in range(2):
        forward(a)
        left(90)
        forward(b)
        left(90)
def move(x, y):
    penup()
    goto(x, y)
    setheading(0)
    pendown()
def colorchange(pencolor, fillcolor):
    end_fill()
    color(pencolor, fillcolor)
    begin_fill()
while(True):
    pen = ["#" + ''.join([choice('ABCDEF0123456789') for i in range(6)])]
    back = ["#" + ''.join([choice('ABCDEF0123456789') for i in range(6)])]
    scale = uniform(0.25, 2)
    move(randint(50 - screensize()[0], screensize()[0] - 100), randint(50 - screensize()[1], screensize()[1] - 100))
    colorchange(pen, back)
    speed(1000)
    rectangle(100*scale, 100*scale)
    move(xcor() + 100*scale, ycor() + 100*scale)
    left(135)
    forward(70.711*scale)
    left(90)
    forward(70.711*scale)
    colorchange(pen, '#00fcf0')
    move(xcor() + 15*scale, ycor() - 30*scale)
    rectangle(20*scale, 20*scale)
    colorchange(pen, '#00fcf0')
    move(xcor() + 50*scale, ycor())
    rectangle(20*scale, 20*scale)
    colorchange(pen, '#593323')
    move(xcor() - 15*scale, ycor() - 70*scale)
    rectangle(20*scale, 40*scale)
    colorchange('#fffb00', '#fffb00')
    move(xcor() + 3*scale, ycor() + 15*scale)
    circle(2.5*scale)
    end_fill()