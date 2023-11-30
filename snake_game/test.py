from turtle import Screen, Turtle
import time


screen = Screen()
screen.tracer(0)

turtle = Turtle(shape="turtle")


def up():
    turtle.setheading(90)


def down():
    turtle.setheading(270)


def left():
    turtle.setheading(180)


def right():
    turtle.setheading(0)


def move():
    turtle.forward(20)

screen.listen()

screen.onkey(up, "Up")
screen.onkey(down, "Down")
screen.onkey(left, "Left")
screen.onkey(right, "Right")

# while True:
#     screen.update()
#     time.sleep(0.1)
#     move()

screen.exitonclick()
