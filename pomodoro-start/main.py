from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
# 25
WORK_MIN = 25
# 5
SHORT_BREAK_MIN = 5
# 20
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global timer
    window.after_cancel(timer)
    #00:00
    canvas.itemconfig(timer_text, text=f"00:00")
    the_label.config(text="Timer", fg=GREEN)
    check_mark.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    # work_sec * 60
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        # If it's the 8th rep
        count_down(long_break_sec)
        # print(f"Sleep break till: {reps}")
        # the_label["text"] = "Break"
        # the_label["fg"] = RED
        the_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        # If it's 2nd, 4th, 6th
        count_down(short_break_sec)
        # print(f"Taking break till: {reps}")
        # the_label["text"] = "Break"
        # the_label["fg"] = PINK
        the_label.config(text="Break", fg=PINK)
    else:
        # If it's the 1st/3rd/5th/7th
        count_down(work_sec)
        # the_label["text"] = "Work"
        # the_label["fg"] = GREEN
        the_label.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    # Add checkmarks
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec == 0:
        count_sec = "00"
    elif count_sec < 10:
        the_count_sec = pow(0, count)
        count_sec = f"{the_count_sec}{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_session = math.floor(reps/2)
        for _ in range(work_session):
            marks += "✓"
        check_mark.config(text=marks)

        # if reps % 2 == 0:
        #     check_mark.config(text="✓", fg=GREEN)
        #     check_mark.grid(column=1, row=3)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Cà chua")
window.config(padx=100, pady=50, bg=YELLOW)

# The label
the_label = Label(text="Work", fg=GREEN, font=(FONT_NAME, 50))
the_label.config(bg=YELLOW)
the_label.grid(column=1, row=0)

# Start and restart button, later command will be included
start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

# Check Mark
check_mark = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 12, "bold"))
check_mark.grid(column=1, row=3)

#


canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

window.mainloop()
