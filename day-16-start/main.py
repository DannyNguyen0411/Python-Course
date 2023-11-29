# import another_module
# print(another_module.another_variable)
#
# from turtle import Turtle, Screen
#
# timmy = Turtle()
# print(timmy)
# timmy.color("Cyan")
# timmy.shape("turtle")
# timmy.forward(100)
#
#
#
# toad = Turtle()
# print(toad)
# toad.shape("turtle")
#
# def dance():
#     toad.forward(100)
#     toad.left(100)
#     toad.forward(100)
#     toad.backward(100)
#     toad.color("DarkGreen")
# dance()
#
# while True:
#     dance()
#
#
# my_screen = Screen()
# my_screen.bgcolor("orange")
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()

print(table.align)
# Add pokemon names in column
table.add_column("Pokemon Name",["Pikachu", "Greninja", "Noivern", "Hawlucha", "Goodra", "Talonflame"],),
# Add types of the pokemon
table.add_column("Type", ["Electric", "Water & Dark", "Flying & Dragon", "Fighting & FLying", "Dragon", "Fire & Flying"])
table.add_column("Gender", ["Male", "Male", "Male", "Male", "Male", "Male"])
# Add shiny form of it
table.add_column("Item hold", ["Light Ball", "", "", "", "", ""])
table.align = "l"

print(table)