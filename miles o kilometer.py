from tkinter import *

def kilometer():
    miles=float(wheel.get())
    kilo= miles * 1.609
    result_kilo.config(text=f"{kilo}")



screen=Tk()
screen.minsize(width=300,height=200)
screen.title("Converter")
screen.config(padx=20,pady=20)

text=Label(text="Miles to Kilometer Converter")
text.grid(column=0,row=0)
#
# input_text = Entry(width=10)
# input_text.grid(column=0,row=1)


wheel=Spinbox(from_=0,to=100)
wheel.grid(column=3,row=1)

text_miles=Label(text=" in miles")
text_miles.grid(column=1,row=1)

button=Button(text="calculate",command=kilometer)
button.grid(column=0,row=3)

result_kilo=Label(text="0")
result_kilo.grid(column=1,row=4)
result_kilo.config(pady=20,padx=20)


text_kilo=Label(text="kilometer is     =")
text_kilo.grid(column=0,row=4)
text_kilo.config(padx=20,pady=20)

screen.mainloop()