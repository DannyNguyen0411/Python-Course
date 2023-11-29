# #Theory / learning 👌
#
# # import turtle
# # from turtle import *
#
# # alias name
# import turtle as t
#
# tommy = t.Turtle()
#
# # Import modules from a bigger library
# import heroes
# print(heroes.gen(    ))


# Line of code starts here 👇
import random
import turtle as t
from turtle import Turtle, Screen

tom = t.Turtle()
tom.shape("turtle")

jerry = Turtle()
jerry.shape("turtle")

spike = Turtle()
spike.shape("turtle")

steps = 0

# def dashed_line():
#     for _ in range(15):
#         # spike.forward(10)
#         # spike.penup()
#         # spike.forward(10)
#         # spike.pendown()
#
#         spike.pencolor("red")
#         spike.forward(5)
#         spike.pencolor("blue")
#         spike.forward(5)
#         spike.penup()
#         spike.forward(10)
#         spike.pendown()
#
# def triange():
#     for _ in range(3):
#         jerry.showturtle()
#         jerry.pencolor("blue")
#         jerry.forward(100)
#         jerry.right(120)
# def square():
#     for _ in range(4):
#         jerry.pencolor("red")
#         jerry.forward(100)
#         jerry.right(90)
# def pentagon():
#     for _ in range(5):
#         jerry.pencolor("green")
#         jerry.forward(100)
#         jerry.right(72)
#
# def hexagon():
#     for _ in range(6):
#         jerry.pencolor("gold")
#         jerry.forward(100)
#         jerry.right(60)
#
# def heptagon():
#     for _ in range(7):
#         jerry.pencolor("aqua")
#         jerry.forward(100)
#         jerry.right(51.5)
#
# def octagon():
#     for _ in range(8):
#         jerry.pencolor("aquamarine")
#         jerry.forward(100)
#         jerry.right(45)
#
# def nonagon():
#     for _ in range(9):
#         jerry.pencolor("crimson")
#         jerry.forward(100)
#         jerry.right(40)
#
# def decagon():
#     for _ in range(10):
#         jerry.pencolor("black")
#         jerry.forward(100)
#         jerry.right(36)
#
# # Create
# def all_shapes():
#     triange()
#     square()
#     pentagon()
#     hexagon()
#     heptagon()
#     octagon()
#     nonagon()
#     decagon()


# #     Other solution
#
# colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         tom.forward(100)
#         tom.right(angle)
#
# for shape_side_n in range(3, 11):
#     tom.color(random.choice(colors))
#     draw_shape(shape_side_n)

# # The shapes
# while not steps == 0:
#     jerry.speed(999999)
#     all_shapes()
#     jerry.hideturtle()
#     steps -= 1


# Dashed line
# while not steps == 0:
#     dashed_line()
#     spike.left(90)
#     dashed_line()
#     spike.left(90)
#     dashed_line()
#     spike.left(90)
#     dashed_line()
#     steps -= 1

# # Tom and Jerry
# while not steps == 0:
#     jerry.speed(2)
#     jerry.fillcolor("brown")
#     jerry.pencolor("blue")
#     tom.speed(1)
#     tom.pencolor("darkgray")
#     tom.fillcolor("gray")
#     square()
#     triange()
#     steps -= 1

# tom.hideturtle()
# jerry.hideturtle()

# characters = [tom, jerry, spike]
# directions = [0, 90, 180, 270]
# t.colormode(255)
#
#
# # colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen",
# #           "MediumPurple", "MediumAquamarine", "Gold", "Tomato", "RoyalBlue", "MediumSpringGreen", "DarkOrange", "MediumSlateBlue"]
# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     random_color = (r, g, b)
#     return random_color

# Testing color
# for _ in range(200):
#     tom.color(random_color())
#     tom.pensize(10)
#     tom.forward(30)
#     tom.right(30)
#     tom.right(30)
#     tom.right(30)

# def random_walk(character):
#     for _ in range(200):
#         character.speed("fastest")
#         character.pensize(10)
#         character.setheading(random.choice(directions))
#         character.color(random_color())
#         character.forward(30)
#
#
# for char in characters:
#     random_walk(char)

# Todo 5. Spiral circular effect
t.colormode(255)


# colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen",
#           "MediumPurple", "MediumAquamarine", "Gold", "Tomato", "RoyalBlue", "MediumSpringGreen", "DarkOrange", "MediumSlateBlue"]
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color

tom.speed("fastest")
def draw_spiralgraph(size_gap):
    for _ in range(int(360 / size_gap)):
        tom.color(random_color())
        tom.circle(100)
        tom.setheading(tom.heading() + size_gap)
        # # Use the following instead solution instead
        # tom.left(5)

draw_spiralgraph(5)

screen = Screen()
screen.exitonclick()
