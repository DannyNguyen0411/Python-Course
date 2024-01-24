from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
FONT_ITALIC = ("Arial", 40, "italic")
FONT_BOLD = ("Arial", 60, "bold")
FRENCH_RAND_WORD = ""

# --------------------------Read data-------------------------------------
data = pandas.read_csv("data/french_words.csv")
to_learn = data.to_dict(orient="records")

# --------------------------The function-------------------------------------

def next_card():
    global FRENCH_RAND_WORD
    current_card = random.choice(to_learn)
    current_word = current_card["French"]
    title = canvas.create_text(400, 150, text="French", font=FONT_ITALIC)
    text = canvas.create_text(400, 263, text=current_word, font=FONT_BOLD)



# def wrong_fun():
#     global FRENCH_RAND_WORD
#     current_card = random.choice(to_learn)
#     print(current_card)

# --------------------------UI Setup-------------------------------------
window = Tk()
window.title("Flash")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_card_img = PhotoImage(file="images/card_front.png")
back_card_img = PhotoImage(file="images/card_back.png")

front_card = canvas.create_image(400, 263, image=front_card_img)

title = canvas.create_text(400, 150, text="Title", font=FONT_ITALIC)
text = canvas.create_text(400, 263, text="Word", font=FONT_BOLD)

canvas.grid(column=0, row=0, columnspan=2)

# Buttons
right_img = PhotoImage(file="images/right.png")
wrong_img = PhotoImage(file="images/wrong.png")

right_button = Button(image=right_img, highlightthickness=0, command=next_card)
wrong_button = Button(image=wrong_img, highlightthickness=0, command=next_card)
right_button.grid(column=1, row=1)
wrong_button.grid(column=0, row=1)




window.mainloop()
