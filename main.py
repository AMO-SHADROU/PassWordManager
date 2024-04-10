import tkinter
from tkinter import messagebox
import random
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    new_data = {
        website_entry.get(): {
            "email": email_entry.get(),
            "password": password_entry.get()
        }
    }
    if len(website_entry.get()) == 0 or len(password_entry.get()) == 0:
        messagebox.showerror("Error", "Please dont leave any blank")
    else:
        # is_ok = messagebox.askokcancel(title=website_entry.get(), message=f"These are the details entered: \n"
        #                                                                   f"Email: {email_entry.get()}\n"
        #                                                                   f"Password: {password_entry.get()}\n"
        #                                                                   f"Is this ok to save?")
        # if is_ok:
        try:
            with open("data.json", "r") as file:
                # reading old data
                data = json.load(file)
        except FileNotFoundError:
            with open("data.json", "w") as file:
                json.dump(new_data, file, indent=4)
        else:
            # updating old data
            data.update(new_data)
            with open('data.json', 'w') as file:
                # saving updated data
                json.dump(new_data, file, indent=4)
        finally:
            website_entry.delete(0, tkinter.END)
            password_entry.delete(0, tkinter.END)
# ---------------------------- FIND PASSWORD------------------------- #


def find_password():
    website = website_entry.get()
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showerror("Error", "No data file found.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showerror("Error", f"No data for {website} exists.")


# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

logo_image = tkinter.PhotoImage(file="logo.png")
canvas = tkinter.Canvas(width=200, height=200)
canvas.create_image(100, 100, image=logo_image)
canvas.grid(row=0, column=1)

website_label = tkinter.Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = tkinter.Label(text="Email/Username:")
email_label.grid(row=2, column=0)
password_label = tkinter.Label(text="Password:")
password_label.grid(row=3, column=0)

website_entry = tkinter.Entry(width=22)
website_entry.grid(row=1, column=1)
website_entry.focus()
email_entry = tkinter.Entry(width=40)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "Amirali.Shadrou@gmail.com")
password_entry = tkinter.Entry(width=22)
password_entry.grid(row=3, column=1)

password_button = tkinter.Button(text="Generate Password", command=generate_password)
password_button.grid(row=3, column=2)
add_button = tkinter.Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)
search_button = tkinter.Button(text="Search", width=15, command=find_password)
search_button.grid(row=1, column=2)

window.mainloop()
