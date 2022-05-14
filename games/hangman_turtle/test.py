from turtle import *
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

draw(0)
done()