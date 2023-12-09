from turtle import Turtle

WIDTH = 1
HEIGHT = 5
# X_POS = -350
# Y_POS = 0


class Paddle(Turtle):
    def __init__(self, x_pos, y_pos):
        super().__init__()
        self.movements = []
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.shape("square")
        self.goto(self.x_pos, self.y_pos)
        self.color('white')
        self.penup()
        self.shapesize(stretch_wid=HEIGHT, stretch_len=WIDTH)

    def go_up(self):
        y = self.ycor()
        y += 30
        self.sety(y)

    def go_down(self):
        y = self.ycor()
        y -= 30
        self.sety(y)
