from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Retro Gaming", 16, "normal")

class Statesboards:

    def __init__(self):
        self.text = Turtle()
        self.text.hideturtle()
        self.text.penup()

    def write_state(self, xcor, ycor, the_state):
        self.text.goto(xcor, ycor)
        self.text.write(f"{the_state}", False, align=ALIGNMENT, font=FONT)

