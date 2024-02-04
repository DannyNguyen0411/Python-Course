from tkinter import *

GREEN = "green"



# ----------------------UI Setup -----------------------------
window = Tk()
window.config(bg=GREEN)

text = Label(text="Hello World!", bg=GREEN, font=("Arial", 20))
text.grid(column=0, row=0)

# Canvas
canvas = Canvas(width=800, height=526)

mlg_image = PhotoImage(file="img/Mlg_Toad.jpg")
image_background = canvas.create_image(400, 400, image=mlg_image)

canvas.grid(column=0, row=0, columnspan=2)


window.mainloop()