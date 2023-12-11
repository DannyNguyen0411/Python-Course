from turtle import Turtle

FONT = ("Retro Gaming", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.score = 1
        self.booster = 5

    def update_score(self):
        self.clear()
        self.goto(-280, 250)
        self.write(f"Level {self.score}", False, align="Left", font=FONT)
        self.goto(280, 250)
        self.write(f"Boosters left {self.booster}", False, align="Right", font=FONT)

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write("GAME OVER", False, align="center", font=FONT)

    def increase_score(self, points):
        self.score += points
        self.update_score()

    def decrease_booster(self, points):
        self.booster -= points
        self.update_score()
