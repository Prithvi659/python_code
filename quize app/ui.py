from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"




class QuizInterface:

    def __init__(self, quiz_brain:QuizBrain):
        self.quiz=quiz_brain

        self.window=Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR,padx=50,pady=50)

        self.score_label=Label(text="Score: 0",font=("Georgia",20,"bold"),bg=THEME_COLOR)
        self.score_label.grid(column=0,row=0,columnspan=2)

        true_image = PhotoImage(file="images/true.png")
        false_image = PhotoImage(file="images/false.png")

        self.canva=Canvas()
        self.canva.create_window(300,300)
        self.canva.grid(column=1,row=1,columnspan=2,pady=50)
        self.question_text=self.canva.create_text(150,150,text="quiz question",font=("Georgia",20,"bold"),width=280)

        self.true_button=Button(image=true_image,highlightthickness=0,command=self.true_pressed)
        self.true_button.grid(column=1,row=3)

        self.false_button=Button(image=false_image,highlightthickness=0,command=self.false_pressed)
        self.false_button.grid(column=2,row=3)

        self.new_question()

        self.window.mainloop()

    def new_question(self):
        self.canva.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text=self.quiz.next_question()
            self.canva.itemconfigure(self.question_text,text=q_text)
        else:
            self.canva.itemconfig(self.question_text,text="You have completed the quiz")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_pressed(self):
        is_right=self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def false_pressed(self):
        is_right=self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self,is_right):
        if is_right:
            self.canva.config(bg="green")
        else:
            self.canva.config(bg="red")

        self.window.after(1000,self.new_question)

