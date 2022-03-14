from tkinter import messagebox
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
import random
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
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
    password_entry.insert(0,password)

    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website_info = website_entry.get()
    usrname_info = usrname_entry.get()
    password_info = password_entry.get()
    if len(website_info) == 0 or len(password_info) == 0:
        messagebox.showwarning(title="empty error",message="Your website and password should not be empty")
    else:
        is_ok = messagebox.askokcancel(title=website_info, message=f"These are the details entered: \nEmail:"
                                                           f"{usrname_info}\nPassword: {password_info}\nIs it ok to save?")

        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website_info} | {usrname_info} | {password_info}\n")
                website_entry.delete(0,END)
                # usrname_entry.delete(0,END)
                password_entry.delete(0,END)

# ---------------------------- UI SETUP ------------------------------- #
from tkinter import *
# FONT = ("Courier", 12, "bold")

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

#logo layout
canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file='logo.png')
canvas.create_image(100,100, image=logo_img)
canvas.grid(column=1, row=0)

#wewbsite layout
website_label= Label(text="Website: ")
website_label.grid(column=0, row=1)

website_entry = Entry(width=38)
website_entry.grid(column=1, columnspan=2, row=1)
website_entry.focus()

#usrname layout
usrname_label = Label(text="Email/Username:")
usrname_label.grid(column=0, row=2)

usrname_entry = Entry(width=38)
usrname_entry.grid(column=1, columnspan=2, row=2)
usrname_entry.insert(0, "example@gmail.com")

#password layout
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

password_entry = Entry(width=19)
password_entry.grid(column=1, row=3)


#button layout
gw_button = Button(text="Generate Password", width=15, command=generate_password)
gw_button.grid(column=2, row=3)

add_button = Button(text="Add", width=33, command=save)
add_button.grid(column=1, columnspan=2, row=4)

window.mainloop()