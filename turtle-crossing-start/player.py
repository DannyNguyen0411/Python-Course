from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def move(self):
        self.forward(MOVE_DISTANCE)

    def next_level(self):
        self.goto(STARTING_POSITION)

    def easter_egg(self):
        self.shapesize(50)
        self.shapesize(1)


    def speed_off(self):
        MOVE_DISTANCE = 30
        self.forward(MOVE_DISTANCE)




