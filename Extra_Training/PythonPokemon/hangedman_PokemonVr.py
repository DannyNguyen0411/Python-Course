# Imported os so it clear the previous screen after you fill in the input
import os
import random
# The art for the intro screen
import hangedman_art 

# Add the words you want to play hangman
import hangedman_word


word_lists = hangedman_word.word_lists
chosen_word_list = random.choice(word_lists)
chosen_word = random.choice(chosen_word_list)


# Logo for the game
logo = hangedman_art.logo
print(logo)

# Begin of the game message
print("Welcome to hangedman 'Pokemon version!")

# Make a new list for display the words
display = []
word_length = len(chosen_word)
for _ in range(word_length):
    display += "_"
print(display)

end_game = False
lives = 6

while not end_game:
    guess = input("Guess a letter: ").lower()

    os.system("cls")
    
    if guess in display:
        print(f"You already guessed the letter '{guess}'")

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
          display[position] = letter
          print(f"Good job! lives remaining: {lives}")

    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that's not the word. You lose a live lives remaining: {lives}")
        if lives <= 0:
            end_game = True
            print(f"You Lose! The word was: {chosen_word}")
    

    print(display)

    if not "_" in display:
        end_game = True
        print("You Win!")
    
    stages = hangedman_art.stages
    print(stages[lives])


        