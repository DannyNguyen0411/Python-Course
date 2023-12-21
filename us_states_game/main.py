import turtle
import pandas
from statesboard import Statesboards

screen = turtle.Screen()
screen.title("Make America Great Again")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
state_board = Statesboards()

# Use the Excel file
data = pandas.read_csv("50_states.csv")
states_data = data.state.to_list()
x_cor_data = data.x.to_list()
y_cor_data = data.y.to_list()
# print(f"{states_data}\n{x_cor_data}\n{y_cor_data}")

guess_states_list = []
x_cor_list = []
y_cor_list = []

# Starts the game with the while loop
game_is_on = True
correct_guessed = 0

while game_is_on and correct_guessed != 5:
    answer_state = screen.textinput(title=f"{correct_guessed}/50 States Correct", prompt="What's another state's name?")
    print(answer_state)
    for guess in states_data:
        if answer_state.title() and guess.title() != 3:
            data_cor = data[data.state == f"{answer_state.title()}"]

            if not data_cor.empty:
                guess_states_list.append(answer_state.title())
                x_cor_list.append(data_cor.x.values[0])
                y_cor_list.append(data_cor.y.values[0])
                state_board.write_state(x_cor_list[-1], y_cor_list[-1], guess_states_list[-1])
                print(guess_states_list)
                print(x_cor_list)
                print(y_cor_list)
                correct_guessed += 1
        else:
            print("Invalid state name. Please try again.")


