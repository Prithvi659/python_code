from tkinter import *
import pandas

BACKGROUND_COLOR = "#B1DDC6"

try:
    data = pandas.read_csv("words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("french_words.csv")

current_card = {}
flip_timer = None


def next_card():
    global current_card, flip_timer

    if len(data) == 0:
        canva.itemconfig(word_text, text="🎉 All words learned!")
        canva.itemconfig(title_text, text="")
        return

    window.after_cancel(flip_timer)

    current_card = data.sample().iloc[0]

    canva.itemconfig(card_image, image=card_front_image)
    canva.itemconfig(title_text, text="French", fill="black")
    canva.itemconfig(word_text, text=current_card["French"], fill="black")

    flip_timer = window.after(3000, flip_card)


def flip_card():
    canva.itemconfig(card_image, image=card_back_image)
    canva.itemconfig(title_text, text="English", fill="red")
    canva.itemconfig(word_text, text=current_card["English"], fill="red")


def correct():
    global data
    data.drop(current_card.name, inplace=True)  #inplace=True changes data permanently,name = whole row of the word
    data.to_csv("words_to_learn.csv", index=False)
    next_card()


def wrong():
    next_card()


# ---------- UI ----------
window = Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

card_front_image = PhotoImage(file="small images/small_Front image.png")
card_back_image = PhotoImage(file="small images/small_back image.png")
right_image = PhotoImage(file="small images/small_right image.png")
wrong_image = PhotoImage(file="small images/small_wrong image.png")

canva = Canvas(width=400, height=264, highlightthickness=0, bg=BACKGROUND_COLOR)
card_image = canva.create_image(200, 132, image=card_front_image)
title_text = canva.create_text(200, 70, font=("Times New Roman", 20, "bold"))
word_text = canva.create_text(200, 150, font=("Times New Roman", 30, "bold"))
canva.grid(column=0, row=0, columnspan=2)

right_button = Button(image=right_image, highlightthickness=0, command=correct)
right_button.grid(column=1, row=1)

wrong_button = Button(image=wrong_image, highlightthickness=0, command=wrong)
wrong_button.grid(column=0, row=1)

flip_timer = window.after(3000, flip_card)
next_card()

window.mainloop()
