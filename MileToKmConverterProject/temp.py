from tkinter import *

root = Tk()
root.title("Temperature converter")
root.minsize(width=500, height=500)
root.config(padx=100, pady=0)


# function
def temp_converter():
    try:
        new_text = the_input.get()
        new_float = float(new_text)

        if -273 <= new_float:
            result_far = round(new_float * 9 / 5 + 32, 2)
            result_kel = round(new_float + 273.15, 2)
            field_one.config(text=result_far)
            field_two.config(text=result_kel)
            text.config(text="Convert the temperatures")
            if -273 == new_float:
                text.config(text="You reached the Absolute Zero!")
            elif 100 >= new_float:
                text.config(text="You changed to steam!")
        elif -273 >= new_float:
            text.config(text="Absolute zero of Celsius is -273!")
        else:
            text.config(text="Please enter a number!")
    except ValueError:
        text.config(text="It has to be a valid number!")


# Label
text = Label(text="Convert the temperatures", font=("Arial", 24))
text.config(pady=20)
text.grid(column=2, row=0)

celsius = Label(text="Celsius", font=("Arial", 12))
celsius.grid(column=2, row=1)

fahrenheit = Label(text="Fahrenheit", font=("Arial", 12))
fahrenheit.grid(column=2, row=2)

kelvin = Label(text="Kelvin", font=("Arial", 12))
kelvin.grid(column=2, row=3)

field_one = Label(text="0", font=("Arial", 12))
field_one.config(padx=30)
field_one.grid(column=1, row=2)

field_two = Label(text="0", font=("Arial", 12))
field_two.config(padx=30)
field_two.grid(column=1, row=3)

# Entry

the_input = Entry(width=10)
the_input.focus()
the_input.grid(column=1, row=1)

# Button

button = Button(text="Calculate", command=temp_converter)
button.grid(column=2, row=4)

root.mainloop()
