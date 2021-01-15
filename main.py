from tkinter import *
from tkinter import messagebox
import re
import json
# generate password
import random


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    # using list comprehension
    password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_symbols = [random.choice(numbers) for _ in range(random.randint(2, 4))]
    password_numbers = [random.choice(symbols) for _ in range(random.randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols
    random.shuffle(password_list)
    password = "".join(password_list)
    password_entry.insert(0, password)


# Check if valid email
def check_email(email):
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    if not re.search(regex, email):
        return True
    else:
        return False


# save to the file
def save():
    website = website_entry.get()
    email = email_entry.get()
    email_not_valid = check_email(email)
    password = password_entry.get()
    new_data = {website: {
        "email": email,
        "password":password
    }}
    if email_not_valid:
        messagebox.showerror(title="email", message="Invalid Email")
    elif len(website) == 0 or len(password) == 0 or len(email) == 0:
        messagebox.showerror(title="email", message="Password, Email and website are Mandatory fields")
    else:
        with open("data.json", "r") as data_file:
            # How to update the json data
            # reading the old data
            data = json.load(data_file)
            # updating old data with new one
            data.update(new_data)

        with open("data.json", "w") as data_file:
            # saving the update data
            json.dump(data, data_file, indent=4)
            website_entry.delete(0, END)
            password_entry.delete(0, END)


window = Tk()

window.title("Password Manager")
window.config(padx=50, pady=50, bg="white")
canvas = Canvas(height=300, width=300, bg="white")

lock_img = PhotoImage(file="icon.png")
canvas.create_image(150, 150, image=lock_img)
canvas.grid(row=0, column=0, columnspan=4)

# left labels1
website_label = Label(text="Website", bg="white")
website_label.grid(row=1, column=0)
email_label = Label(text="Email", bg="white")
email_label.grid(row=2, column=0)
password_label = Label(text="Password", bg="white")
password_label.grid(row=3, column=0)

# Entries
website_entry = Entry(width=45)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()
email_entry = Entry(width=45)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "testing@hotmail.com")
password_entry = Entry(width=26)
password_entry.grid(row=3, column=1)

# buttons
generate_password_button = Button(text="Generate Password", width=15, command=generate_password)
generate_password_button.grid(row=3, column=2)
add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
