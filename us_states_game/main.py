import turtle
import pandas

screen = turtle.Screen()
screen.title("Make America Great Again")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


answer_state = screen.textinput(title="Guess a state", prompt="What's another state's name?")
print(answer_state)