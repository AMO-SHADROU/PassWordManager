import tkinter
from tkinter import messagebox
import random
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v'
        , 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S'
        , 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for char in range(nr_letters)]
    password_numbers = [random.choice(numbers) for num in range(nr_numbers)]
    password_symbols = [random.choice(symbols) for symbol in range(nr_symbols)]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    if len(website_entry.get()) == 0 or len(password_entry.get()) == 0:
        messagebox.showerror("Error", "Please dont leave any blank")
    else:
        is_ok = messagebox.askokcancel(title=website_entry.get(), message=f"These are the details entered: \n"
                                                                          f"Email: {email_entry.get()}\n"
                                                                          f"Password: {password_entry.get()}\n"
                                                                          f"Is this ok to save?")
        if is_ok:
            with open('data.txt', 'a') as file:
                file.write(f"{website_entry.get()} | {email_entry.get()} | {password_entry.get()}\n")
                website_entry.delete(0, tkinter.END)
                password_entry.delete(0, tkinter.END)


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

website_entry = tkinter.Entry(width=40)
website_entry.grid(row=1, column=1, columnspan=2)
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

window.mainloop()
