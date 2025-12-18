from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
check_mark="✔"
reps=0
timer=None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    label_timer.config(text="Timer")
    text.config(text="")
    global reps
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    reps += 1

    work_secs=WORK_MIN * 60
    short_break_secs=SHORT_BREAK_MIN * 60
    long_break_secs=LONG_BREAK_MIN * 60

    if reps == 1 or reps == 3 or reps == 5 or reps == 7:
        countdown(work_secs)
        label_timer.config(text="Work",fg=GREEN)
    elif reps == 2 or reps == 4 or reps == 6:
        countdown(short_break_secs)
        label_timer.config(text="Short Break",fg=PINK)
    else:
        countdown(long_break_secs)
        label_timer.config(text="Long Break",fg=RED)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def countdown(count):
    mins=math.floor(count/60)
    secs=count % 60
    if secs < 10:
        secs = f"0{secs}"

    canvas.itemconfig(timer_text,text=f"{mins}:{secs}")
    if count > 0:
        global timer
        timer=window.after(1000,countdown,count-1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            marks += "✔"
        text.config(text=marks)





# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("Pomodoro")
window.config(pady=50,padx=100,bg=YELLOW)

label_timer=Label(text="Timer",fg=GREEN,font=(FONT_NAME,20,"bold"),highlightthickness=0,bg=YELLOW)
label_timer.grid(column=1,row=0)

start_button=Button(text="Start",command=start_timer)
start_button.grid(column=0,row=2)

reset_button=Button(text="Reset",command=reset_timer)
reset_button.grid(column=3,row=2)

text=Label(fg=GREEN,bg=YELLOW)
text.grid(column=1,row=3)

canvas=Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
tomato=PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=tomato)
timer_text=canvas.create_text(100,130,text="00.00",font=(FONT_NAME,30,"bold"),fill="white")
canvas.grid(column=1,row=1)


window.mainloop()

