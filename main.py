from tkinter import*
from tkinter import messagebox
from random import *
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(4, 7))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 3))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 3))]

    password_list =  password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0,password)
    pyperclip.copy(password)
# ---------------------------- BRAIN ------------------------------- #
def save():
    website = web_entry.get()
    user = username_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "Email" : user,
            "Password" : password,
        }
    }
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops",message="Please don't leave any fields empty!")
    else:
        try:
            with open("data.json","r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json","w") as data_file:
                json.dump(new_data,data_file,indent=4)
        else:
            data.update(new_data)
            with open("data.json","w") as data_file:
                json.dump(data,data_file,indent=4)
        finally:
            web_entry.delete(0,END)
            password_entry.delete(0,END)
def find_password():
        website = web_entry.get()
        try:
            with open("data.json") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            messagebox.showinfo(title="Error",message="No data file found")
        else:
            if website in data:
                email = data[website]["Email"]
                my_password = data[website]["Password"]
                messagebox.showinfo(title=website,message=f"Email: {email}\nPassword: {my_password}")
            else:
                messagebox.showinfo(title="Error",message=f"No details for {website} exists.")
# ---------------------------- UI SETUP ------------------------------- #
root = Tk()
root.title("Password Manager")
root.geometry("900x900")

bg_image = PhotoImage(file="backdrop.png")
bg_label = Label(root, image=bg_image)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)


my_website = Label(bg_label, text="Website:", fg="#00FFCC", bg="#000000", font=("Orbitron", 10, "bold"))
my_website.place(relx=0.2, y=450, anchor="n")

web_entry = Entry(bg_label, fg="#00FFCC",width=38,bg="#000000",insertbackground="#00FFCC")
web_entry.place(relx=0.471,y=450,anchor="n")
web_entry.focus()

search_button = Button(text="Search",width=16,fg="#00FFCC",bg="#000000",font=("Orbitron", 10),command=find_password)
search_button.place(relx=0.739,y=450,anchor="n")

username_email = Label(bg_label, text="Username/E-mail:", fg="#00FFCC", bg="#000000", font=("Orbitron", 10, "bold"))
username_email.place(relx=0.2, y=500, anchor="n")

username_entry = Entry(bg_label, fg="#00FFCC",width=58,bg="#000000",insertbackground="#00FFCC")
username_entry.place(relx=0.56,y=500,anchor="n")
username_entry.insert(0,"manojkumarvk748@gmail.com")

password = Label(bg_label, text="Password:", fg="#00FFCC", bg="#000000", font=("Orbitron", 10, "bold"))
password.place(relx=0.2, y=550, anchor="n")

password_entry = Entry(bg_label, fg="#00FFCC",width=38,bg="#000000",insertbackground="#00FFCC")
password_entry.place(relx=0.471,y=550,anchor="n")

password_button = Button(text="Generate Password",fg="#00FFCC",bg="#000000", font=("Orbitron", 10),command=password_generator)
password_button.place(relx=0.739,y=550,anchor="n")

password_add_button = Button(text="Add",fg="#00FFCC",bg="#000000", font=("Orbitron", 10),width=10,command=save)
password_add_button.place(relx=0.5,y=600,anchor="n")
root.mainloop()
