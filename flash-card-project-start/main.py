from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
FONT_ITALIC = ("Arial", 40, "italic")
FONT_BOLD = ("Arial", 60, "bold")
TIMER = None

# --------------------------Read data-------------------------------------
data = pandas.read_csv("data/french_words.csv")
to_learn = data.to_dict(orient="records")
print(to_learn)

french_words = []
english_words = []
language_words = []

for key in to_learn:
    french_words.append(key["French"])
    english_words.append(key["English"])
print(french_words, english_words)
current_card = {}

# US map to see how to convert to "to_csv"

data_dict_words_now = {
    "French": french_words,
    "English": english_words,
}

data_list_words_now = [f"{french_words}+{english_words}\n"]


# --------------------------The function-------------------------------------
def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(title, text="French", fill="black", font=FONT_ITALIC)
    canvas.itemconfig(text, text=current_card["French"], fill="black", font=FONT_BOLD)
    canvas.itemconfig(card_background, image=front_card_img)
    flip_timer = window.after(3000, func=flip_card)

    # data_dictator = data_list_words_now.remove("partie")
    data_info_words = pandas.DataFrame(data_list_words_now)
    data_info_words.to_csv("data/words_to_learn.csv", index= False)


def flip_card():
    canvas.itemconfig(title, text="English", fill="white", font=FONT_ITALIC)
    canvas.itemconfig(text, text=current_card["English"], fill="white", font=FONT_BOLD)
    canvas.itemconfig(card_background, image=back_card_img)


def wrong_card():
    canvas.itemconfig(title, text="English", font=FONT_ITALIC)
    canvas.itemconfig(text, text=current_card["French"], font=FONT_BOLD)
    canvas.itemconfig(card_background, image=back_card_img)
    data_info_words = pandas.DataFrame(data_dict_words_now)
    data_info_words.to_csv("data/words_to_learn.csv")


# --------------------------UI Setup-------------------------------------
window = Tk()
window.title("Flash")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_card_img = PhotoImage(file="images/card_front.png")
back_card_img = PhotoImage(file="images/card_back.png")

card_background = canvas.create_image(400, 263, image=front_card_img)

title = canvas.create_text(400, 150, text="Title", font=FONT_ITALIC)
text = canvas.create_text(400, 263, text="Word", font=FONT_BOLD)

canvas.grid(column=0, row=0, columnspan=2)

# Buttons
right_img = PhotoImage(file="images/right.png")
wrong_img = PhotoImage(file="images/wrong.png")

right_button = Button(image=right_img, highlightthickness=0, command=next_card)
wrong_button = Button(image=wrong_img, highlightthickness=0, command=wrong_card)
right_button.grid(column=1, row=1)
wrong_button.grid(column=0, row=1)

next_card()

window.mainloop()
