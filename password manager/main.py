import json
from tkinter import *
from tkinter import messagebox
from random import randint,choice,shuffle

#Password Generator
def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    # for char in range(nr_letters):
    #   password_list.append(random.choice(letters))
    password_letters=[choice(letters) for _ in range(randint(8,10))]

    password_symbols=[choice(symbols) for _ in range(randint(2,4))]

    password_numbers=[choice(numbers)  for _ in range(randint(2,4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    # for char in password_list:
    #   password += char
    password_entry.delete(0,END)
    password_entry.insert(0,password)

# ----save password

def add_info():
    website=website_entry.get()
    password=password_entry.get()
    email=email_entry.get()
    new_data={
        website:{
        "email":email,
        "password":password
        }}
    if len(website) > 0 and len(password) > 0 and len(email) > 0:
        output=messagebox.askyesno(title="Save Password",message="Do You Want To Continue")
        if output:
            try:
                with open("Password Manager.json","r") as saved_password:
                    data = json.load(saved_password)  # reading json data,mode=r

            except FileNotFoundError:
                with open("Password Manager.json" , "w") as saved_password:
                    json.dump(new_data,saved_password,indent=4)  #write JSON data first create the file

            else:
                data.update(new_data)                         #updateing the data
                with open("Password Manager.json", "w") as saved_password:
                    json.dump(data,saved_password,indent=4)   #saving the data

            finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)
    else:
        messagebox.showerror(title="Error",message="You Left The Field's Empty")

#---- search the data----

def search_data():
    search_website=website_entry.get()
    try:
        with open("Password Manager.json") as data_file:
            data=json.load(data_file)
    except FileNotFoundError:
         messagebox.showerror(title="Error",message=f" data File Not Found")
    else:
        if search_website in data:
            search_email=data[search_website]["email"]
            search_password=data[search_website]["password"]
            messagebox.showinfo(title="website found ",message=f"Email: {search_email} \n Password: {search_password}")
        else:
            messagebox.showerror(title="Error",message=f"Website {search_website} not found")




#---- UI----

window=Tk()
window.title("Password Manager")
window.config(pady=20,padx=20)

logo=PhotoImage(file="logo.png")
canvas=Canvas(width=200,height=200)
canvas.create_image(100,100,image=logo)
canvas.grid(column=1,row=1)


wedsite_label=Label(text="Wedsite Name")
wedsite_label.grid(column=0,row=2)

website_entry=Entry(width=35)
website_entry.grid(column=1,row=2,columnspan=1)
website_entry.focus()



email_label=Label(text="Email/Username")
email_label.grid(column=0,row=3)

email_entry=Entry(width=35)
email_entry.grid(column=1,row=3,columnspan=1)

password_label=Label(text="Password")
password_label.grid(column=0,row=4)

password_entry=Entry(width=35)
password_entry.grid(column=1,row=4,columnspan=1)

password_button=Button(text="Generate Password",command=password_generator)
password_button.grid(column=2,row=4)

add_button=Button(text="Add",width=20,command=add_info)
add_button.grid(column=1,row=5)

search_button=Button(text="Search",width=10,command=search_data)
search_button.grid(column=2,row=2)



window.mainloop()
