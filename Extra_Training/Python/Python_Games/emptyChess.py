import random

# Define the initial grid
row1 = ["🙂", "🙂", "🙂"]
row2 = ["🙂", "🙂", "🙂"]
row3 = ["🙂", "🙂", "🙂"]
game_map = [row1, row2, row3]

# Print the initial grid
print(f"{row1}\n{row2}\n{row3}")

# Get the user's input for the treasure placement
position = input("Where do you want to place the treasure? (e.g., 11 for the top-left corner): ")

# Parse the user's input
horizontal = int(position[0]) - 1
vertical = int(position[1]) - 1

# Place the treasure on the grid
game_map[vertical][horizontal] = "X"

# Computer's turn (randomly guessing)
computer_horizontal = random.randint(0, 2)
computer_vertical = random.randint(0, 2)

# Check if the computer guessed the correct location
if game_map[computer_vertical][computer_horizontal] == "😡":
    print("Computer found the treasure!")
else:
    print("Computer missed the treasure.")

# Print the updated grid
print(f"{row1}\n{row2}\n{row3}")
