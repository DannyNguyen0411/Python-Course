from tkinter import *


def button_clicked():
    print("Button is clicked!")
    new_text = the_input.get()
    my_label.config(text=new_text)


window = Tk()
window.title(f"My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=100, pady=200)

# Label
my_label = Label(text="I'm a fucking Label!", font=("Arial", 24))
# my_label.pack()

# Update the create component
my_label["text"] = "New Text"
my_label.config(text="New Text", padx=50, pady=50)
# my_label.place(x=125, y=125)
my_label.grid(column=0, row=0)
# Button


button = Button(text="Click me", command=button_clicked)
# button.pack()
button.grid(column=1, row=1)

button_two = Button(text="The One Ultimate")
button_two.grid(column=2, row=0)

# Entry
the_input = Entry(width=10, validatecommand="test")
the_input.insert(END, "Some text in here")
# the_input.pack()
the_input.grid(column=3, row=3)



# import turtle
#
# tim = turtle.Turtle()
# tim.penup()
# tim.write("Arguments with Default Values", font=("Times New Roman", 80, "bold"), align="left")


window.mainloop()
