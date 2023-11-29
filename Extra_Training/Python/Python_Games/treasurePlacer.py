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

position_int = len(position)

horizal = int(position[0] - 1)
vertical = int(position[0] - 1)

game_map[vertical][horizal] = "X"

print(f"{row1}\n{row2}\n{row3}")
