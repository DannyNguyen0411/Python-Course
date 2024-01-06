from tkinter import *

window = Tk()
window.title(f"My First GUI Program")
window.minsize(width=500, height=300)

# Label
my_label = Label(text="I'm a fucking Label!", font=("Arial", 24))
my_label.pack()

# Update the create component
my_label["text"] = "New Text"
my_label.config(text="New Text")


# Button
def button_clicked():
    print("Button is clicked!")
    new_text = the_input.get()
    my_label.config(text=new_text)


button = Button(text="Click me", command=button_clicked)
button.pack()

# Entry
the_input = Entry(width=10, validatecommand="test")
the_input.insert(END, "Click on me!")
the_input.pack()


# import turtle
#
# tim = turtle.Turtle()
# tim.penup()
# tim.write("Arguments with Default Values", font=("Times New Roman", 80, "bold"), align="left")


window.mainloop()
