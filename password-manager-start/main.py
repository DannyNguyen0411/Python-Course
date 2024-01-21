from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

FONT_NAME = "Arial"


# image pading 20, width: 200, height: 200
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '<', '>', '?', '/', ',', '\\', '|',
               '{', '}', '[', ']', ';', ':', "'", '"']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols
    shuffle(password_list)

    password = "".join(password_list)

    print(f"Your password is: {password}")
    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if len(email) == 0:
        messagebox.showinfo(title="NOOOOOOOOOO!", message="don't leave it empty! I almost got your IP address😡!!!")
    elif len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        try:
            with open("data.json", mode="r") as data_file:
                # Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                # Saving updated data
                json.dump(new_data, data_file, indent=4)
                print("data.json, not existing. Created new one!")
        else:
            # Updating old data to new data
            data.update(new_data)

            with open("data.json", "w") as data_file:
                # Saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- Find Password ------------------------------- #
def find_password():
    website = website_entry.get()
    found = False

    try:
        with open("data.json", mode="r") as data_file:
            data = json.load(data_file)
            print(data)
            for item, sub_item in data.items():
                if website == item:
                    messagebox.showinfo(title=website,
                                        message=f"The email: {sub_item["email"]}\nThe password: {sub_item["password"]}")
                    found = True
            if not found:
                messagebox.showinfo(title="No website found", message=f"No details for {website} exist.")
                # found = False
    except FileNotFoundError:
        messagebox.showinfo("Error", "No data found!\nFile is not existed yet.")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=20)

# Image
canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="Website:", font=(FONT_NAME, 12))
website_label.grid(column=0, row=1)
email_label = Label(text="Email/Username:", font=(FONT_NAME, 12))
email_label.grid(column=0, row=2)
password_label = Label(text="Password:", font=(FONT_NAME, 12))
password_label.grid(column=0, row=3)

# Entries
website_entry = Entry(window, width=35)
website_entry.focus()
website_entry.grid(column=1, row=1, columnspan=2)
email_entry = Entry(window, width=35)
email_entry.insert(0, "sussysimper@gmail.com")
email_entry.grid(column=1, row=2, columnspan=2)
password_entry = Entry(window, width=21)
password_entry.grid(column=1, row=3)

# Buttons
search = Button(text="Search", command=find_password, width=15)
search.config(padx=0, pady=0)
search.grid(column=2, row=1)

generate_password = Button(text="Generate Password", command=generate_password)
generate_password.config(padx=0, pady=0)
generate_password.grid(column=2, row=3)

# Add delete function
add = Button(text="Add", width=36, command=save)
add.grid(column=1, row=4, columnspan=2)

window.mainloop()
