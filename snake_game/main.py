from turtle import Screen, Turtle

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Metal Gear Solid Snake")

starting_positions = [(0, 0), (-20, 0), (-40, 0)]

# Create new segment for the
for position in starting_positions:
    new_segment = Turtle(shape="square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(position)






















screen.exitonclick()