# import classes
import turtle
from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.bgpic("Neo_Toad.gif")
screen.setup(500, 400)
user_bet = screen.textinput("Make your bet", "Which turtle will win the race? Enter a color: ").lower()
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
y_position = [-100, -70, -40, -10, 20, 50]
all_turtles = []

# The turtles of the turtle class

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(-230, y_position[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The winner is {winning_color} turtle!")
            else:
                print(f"You've lost! The winner is {winning_color} turtle!")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)
# Turtle will move to the start line






screen.exitonclick()