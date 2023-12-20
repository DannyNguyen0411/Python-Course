import turtle
import pandas

screen = turtle.Screen()
screen.title("Make America Great Again")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Use the Excel file
data = pandas.read_csv("50_states.csv")
states_data = data.state.to_list()
x_cor_data = data.x.to_list()
y_cor_data = data.y.to_list()
print(f"{states_data}\n{x_cor_data}\n{y_cor_data}")

guess_states_list = []
x_cor_list = []
y_cor_list = []

# Starts the game with the while loop
game_is_on = True
correct_guessed = 0

test = input("What's your name? ")
print(test.upper())

while game_is_on and correct_guessed != 5:
    answer_state = screen.textinput(title=f"{correct_guessed}/50 States Correct", prompt="What's another state's name?")
    print(answer_state)
    for guess in states_data:
        if answer_state.upper() == guess.upper():
            data_cor = data[data.state == f"{answer_state}"]
            guess_states_list.append(answer_state)
            print(data_cor)
            print(guess_states_list)
            correct_guessed += 1

