from turtle import Turtle

FONT = ("Retro Gaming", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.score = 1

    def update_score(self):
        self.clear()
        self.goto(-230, 240)
        self.write(f"Level {self.score}", False, align="center", font=FONT)

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write("GAME OVER", False, align="center", font=FONT)

    def increase_score(self, points):
        self.score += points
        self.update_score()
