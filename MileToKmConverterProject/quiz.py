from tkinter import *

root = Tk()
root.title("Temperature converter")
root.minsize(width=500, height=500)
root.config(padx=100, pady=0)

# Label
header = Label(text="What are you afraid of right now? Select one box", font=("Arial", 24))
header.grid(column=2, row=0)

text = Label(text="The tip will be written to guide you life to the fullest", font=("Arial", 12))
text.grid(column=2, row=3)
def radio_used():
    print(radio_state.get())
    current_state = radio_state.get()
    if current_state == 1:
        text.config(text=f"It's okay to be afraid of something. You're afraid of failure,\n because you don't know what is lay behind the walls,\n text the girl you have a crush on but you don't know what will happen or how she will react.\n"
                         f"To get passed or break the wall is by facing your fear, fight the boss and conquer or save a world,\n because there is no perfect moment that wait for you! Wake up to the reality💪!")
    elif current_state == 2:
        text.config(text=f"You're are afraid to get out the bubble.\n Listen! When you have trouble getting out of bed,\n tell yourself: "+" I've "+"to go to work as a human being, but you decided to stay in your bed. So you were born to feel nice?\n"
                         f"Instead of doing things and experiencing them?\n Don't you see the plants, the birds, the ants and spiders and bees doing their invidual tasks!\n Start small by setting a task and promise to you! (The quote is by Marcus Aurelius)")
    elif current_state == 3:
        text.config(text=f"So you are afraid of nothing? Good! To make sure you are not truly afraid of something by taking other risks.")

# Variable to hold on to which radio button value is checked.
radio_state = IntVar()
radiobutton1 = Radiobutton(text="Failure", value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="Discomfort-zone", value=2, variable=radio_state, command=radio_used)
radiobutton3 = Radiobutton(text="Nothing", value=3, variable=radio_state, command=radio_used)
radiobutton1.grid(column=1, row=2)
radiobutton2.grid(column=2, row=2)
radiobutton3.grid(column=3, row=2)


root.mainloop()