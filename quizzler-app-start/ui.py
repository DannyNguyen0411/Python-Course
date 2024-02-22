from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")
NUM = 0


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        # ------------------Startup the Tkinter-------------------------
        self.window = Tk()
        self.window.title("Rizzler")
        self.window.config(width=600, height=500, bg=THEME_COLOR, padx=20, pady=20)
        # ------------------Score-------------------------
        self.score_label = Label(text=f"Score: {NUM}", fg="white", bg=THEME_COLOR)
        self.score_label.grid(column=2, row=0, columnspan=2)
        # ------------------Canvas-------------------------
        self.canvas = Canvas(self.window, width=300, height=250, highlightthickness=0, background="white")
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="Some question text",
            fill=THEME_COLOR,
            font=FONT)
        self.canvas.grid(column=1, row=1, columnspan=2, padx=20, pady=50)
        # ------------------Buttons-------------------------
        true_img = PhotoImage(file="images/true.png")
        false_img = PhotoImage(file="images/false.png")
        self.true_button = Button(image=true_img, bg="green", highlightthickness=0, command=self.choose_true)
        self.false_button = Button(image=false_img, bg="red", highlightthickness=0, command=self.choose_false)
        self.true_button.grid(column=1, row=2, padx=20)
        self.false_button.grid(column=2, row=2, padx=20)

        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.score_label.config(text=f"Score: {self.quiz.score}")
            self.canvas.config(bg="white")
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")


    def choose_true(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def choose_false(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000, self.get_next_question)
