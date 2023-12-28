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
missing_states_list = []
x_cor_list = []
y_cor_list = []

# Starts the game with the while loop
game_is_on = True
correct_guessed = 0

while game_is_on and correct_guessed != 50:
    answer_state = screen.textinput(title=f"{correct_guessed}/50 States Correct", prompt="What's another state's name?").title()
    print(answer_state)
    if answer_state == "Exit":
        missing_states = [missing_states_list.append(state) for state in states_data if state not in guess_states_list]
        print(missing_states)
        break
    else:
        if answer_state in states_data:
            data_cor = data[data.state == f"{answer_state.title()}"]
            if answer_state not in guess_states_list:
                guess_states_list.append(answer_state.title())
                x_cor_list.append(data_cor.x.item())
                y_cor_list.append(data_cor.y.item())
                state_board.write_state(x_cor_list[-1], y_cor_list[-1], guess_states_list[-1])
                correct_guessed += 1
                print(guess_states_list)
                print(x_cor_list)
                print(y_cor_list)
            elif answer_state in guess_states_list:
                print("States is already guessed!")
            else:
                print("Invalid state name. Please try again.")

print(f"You guessed {correct_guessed} out of 50")
# missing_states_list = states_data - guess_states_list

# # Other method to solve it
# missing_states_list = list(set(states_data) - set(guess_states_list))

#     states to learn.csv
data_dict_states = {
    "Missing States": missing_states_list,
}

data_info_states = pandas.DataFrame(data_dict_states)
data_info_states.to_csv("missing_states.csv")

print(data_dict_states)

