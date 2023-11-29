# Import stuffs

import turtle as t
import random
from turtle import Turtle, Screen

canvas = Screen()
canvas.screensize(800, 800)
canvas.bgcolor("CornflowerBlue")
canvas.bgpic("richter-belmont-castlevania.gif")

tom = t.Turtle()

t.colormode(255)

color_list = [(213, 154, 96), (52, 107, 132), (179, 77, 31), (202, 142, 31), (115, 155, 171), (124, 79, 99),
              (122, 175, 156), (229, 236, 239), (226, 198, 131), (242, 247, 244), (192, 87, 108), (11, 50, 64),
              (55, 38, 19), (45, 168, 126), (47, 127, 123), (200, 121, 143), (168, 21, 29), (228, 92, 77),
              (244, 162, 160), (38, 32, 35), (2, 25, 24), (78, 147, 171), (170, 23, 18), (19, 79, 90), (101, 126, 158),
              (235, 166, 171), (177, 204, 185), (49, 62, 84)]

the_list = []


def the_colors():
    return color_list

tom.hideturtle()
tom.speed("fastest")


def ten_dots():
    for color in range(10):
        colors = the_colors()
        tom.color(random.choice(colors))
        tom.dot(20)
        tom.forward(50)


def print_dots(dots_position):
    tom.penup()
    for _ in range(10):
        tom.goto(-300 + dots_position, - 200 + 40 * _)
        ten_dots()


print_dots(100)

# def draw_spiralgraph(size_gap):
#     for _ in range(int(360 / size_gap)):
#         colors = the_colors()
#         tom.color(colors[_ % len(colors)])
#         tom.circle(100)
#         tom.setheading(tom.heading() + size_gap)
#
# draw_spiralgraph(5)


canvas.exitonclick()
