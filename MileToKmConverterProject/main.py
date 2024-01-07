from tkinter import *

window = Tk()
window.title("Miles to Km converter")
window.minsize(width=500, height=250)
window.config(padx=100, pady=0)

# miles -> km = 1 * 1.609344
def miles_to_km():
    try:
        new_text = the_input.get()
        new_float = float(new_text)

        if 0 <= new_float:
            result = round(new_float * 1.609344, 2)
            the_output.config(text=result)
        else:
            the_output.config(text="Please enter a number!")
    except ValueError:
        the_output.config(text="It has to be a valid number!")


# Label
text = Label(text="Convert Miles to Km", font=("Arial", 24))
text.config(pady=50)
text.grid(column=3, row=0)

miles = Label(text="Miles", font=("Arial", 12))
miles.grid(column=4, row=2)

km = Label(text="Km", font=("Arial", 12))
km.grid(column=4, row=3)

equals_to = Label(text="is equal to", font=("Arial", 12))
equals_to.grid(column=2, row=3)

# Button
button = Button(text="Calculate", font=("Arial", 12), command=miles_to_km)
button.grid(column=3, row=4)

# The numbers (int)
the_input = Entry(width=10)
the_input.focus()
the_input.grid(column=3, row=2)

the_output = Label(text=0, font=("Arial", 12))
the_output.grid(column=3, row=3)

window.mainloop()
