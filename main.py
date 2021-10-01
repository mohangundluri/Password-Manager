from random import randint, choice
from tkinter import *
from tkinter import messagebox
import json

font = ("Courier", 15, "bold")


window = Tk()
window.title("PASSWORD MANAGER")
window.config(padx=20, pady=20)

image = PhotoImage(file='logo.png')

canvas = Canvas(height=200, width=200)
canvas.create_image(100, 100, image=image)
canvas.grid(column=1, row=0)


def save():

    website_name = website_entry.get()
    email_name = email_entry.get()
    password = password_entry.get()
    new_data = {
        website_name: {
            "email": email_name,
            'password': password,
            }
        }

    if len(website_name) == 0 or len(password) == 0:
        messagebox.showwarning(title="warning", message="Don't leave the fields")
    else:
        try:
            with open('password.json', "r") as data_file:
                data = json.load(data_file)

        except FileNotFoundError:
            with open("password.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)
            with open("password.json", 'w') as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


def password_create():
    list_alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
                      's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    list_numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    list_symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")"]
    no_of_alphabets = randint(6, 8)
    no_of_symbols = randint(3, 5)
    no_of_numbers = randint(3, 5)

    alphabets = [choice(list_alphabets) for _ in range(no_of_alphabets)]
    symbols = [choice(list_symbols)for _ in range(no_of_symbols)]
    numbers = [str(choice(list_numbers)) for _ in range(no_of_numbers)]
    password_generated = alphabets + numbers + symbols
    password_created = "".join(password_generated)
    password_entry.insert(0, f"{password_created}")


def search():
    website = website_entry.get()

    try:
        with open("password.json", "r")as data_file:
            data = json.load(data_file)
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            is_ok = messagebox.showinfo(title=website, message=f'Email is {email}\nPassword {password}')
        else:
            messagebox.showinfo(title="Error", message='No details found')
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="File not found")


website_label = Label(text="Website")
website_label.grid(column=0, row=1)
website_entry = Entry(width=33)
website_entry.grid(column=1, row=1)
website_entry.focus()


email_label = Label(text="Email/Username")
email_label.grid(column=0, row=2)
email_entry = Entry(width=52)
email_entry.grid(columnspan=2, column=1, row=2)
email_entry.focus()
email_entry.insert(0, "mohangundluri@gmail.com")

password_label = Label(text="Password")
password_label.grid(column=0, row=3)
password_entry = Entry(width=33)
password_entry.grid(column=1, row=3)
password_entry.focus()


generate_password = Button(text="Generate Password", command=password_create, fg="red", activeforeground="green",
                           bg="#FFFFB3")
generate_password.grid(column=2, row=3)

add_button = Button(text="Add", width=44, command=save, fg="red", activeforeground="green", bg="#FFFFB3")
add_button.grid(column=1, row=4, columnspan=2)

search_button = Button(text='Search', width=15, fg="red", activeforeground="green", bg="#FFFFB3", command=search)
search_button.grid(column=2, row=1)

window.mainloop()