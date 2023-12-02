from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Retro Gaming", 16, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(0, 260)
        self.write(f"Score: {self.score}", False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", False, align=ALIGNMENT, font=FONT)
    def increase_score(self, points):
        self.score += points
        self.update_score()
