from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project
def generate_pass():
    password_input.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)
    pass_letter = [random.choice(letters) for _ in range(0, nr_letters)]
    pass_sym = [random.choice(symbols) for _ in range(0, nr_symbols)]
    pass_num = [random.choice(numbers) for _ in range(0, nr_numbers)]
    # for n in range(0,nr_letters):
    #     # pass_letter += letters[random.randint(0,len(letters)-1)]
    #     # pass_letter += random.choice(letters)
    # #     pass_letter.append(random.choice(letters))
    # for n in range(0,nr_symbols):
    #     pass_sym += symbols[random.randint(0,len(symbols)-1)]
    # for n in range(0,nr_numbers):
    #     pass_num += numbers[random.randint(0,len(numbers)-1)]
    pass_sum = pass_letter + pass_num + pass_sym
    random.shuffle(pass_sum)
    password_hard = "".join(pass_sum)
    # password_easy = ""
    # for n in pass_sum:
    #     password_easy += n
    # print(password_easy)
    # Eazy Level - Order not randomised:
    # e.g. 4 letter, 2 symbol, 2 number = JduE&!91
    password_input.insert(END, string=password_hard)
    pyperclip.copy(password_hard)


# ---------------------------- SEARCH COMMAND ------------------------------- #
def search_command():
    web = website_input.get()
    try:
        with open("data.json", "r") as file:
            data_json = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title=f"{web}", message="No data file found")
    else:
        if web in data_json:
            email = data_json[web]["email"]
            password = data_json[web]["password"]
            messagebox.showinfo(title=f"{web}", message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title=f"{web}", message=f"No details for {web} exist.")


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    web = website_input.get()
    email_user = email_user_input.get()
    password = password_input.get()
    if len(web) == 0 or len(email_user) == 0 or len(password) == 0:
        messagebox.showerror(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        is_ok = messagebox.askokcancel(title=web, message=f"These are the details entered: \nEmail: {email_user}"
                                                          f"\nPassword: {password} \nIs it ok to save?")
        if is_ok:
            # with open("data.txt", "a") as file:
            #     data = file.write(f"{web} | {email_user} | {password}\n")
            new_data = {
                web: {
                    "email": email_user,
                    "password": password,
                }
            }
            # read and update
            try:
                with open("data.json", "r") as file_json:
                    data = json.load(file_json)
            # save update data
            except FileNotFoundError:
                with open("data.json", "w") as file_json:
                    json.dump(new_data, file_json, indent=4)
            else:
                data.update(new_data)
                with open("data.json", "w") as file_json:
                    json.dump(data, file_json, indent=4)
            finally:
                website_input.delete(0, END)
                password_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg="white")
# img
canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
my_pass_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=my_pass_img)
canvas.grid(column=1, row=0)
# web
website_label = Label(text="Website:", bg="white")
website_label.grid(column=0, row=1)
website_input = Entry(width=33, bg="white")
website_input.grid(column=1, row=1)
website_input.focus()
# email/username
email_user_label = Label(text="Email/Username:", bg="white")
email_user_label.grid(column=0, row=2)
email_user_input = Entry(width=52, bg="white")
email_user_input.grid(column=1, row=2, columnspan=2)
email_user_input.insert(END, string="Boss@gmail.com")
# password
password_label = Label(text="Password:", bg="white")
password_label.grid(column=0, row=3)
password_input = Entry(width=33, bg="white")
password_input.grid(column=1, row=3)
# generate
generate_pass_button = Button(text="Generate Password", bg="white", command=generate_pass)
generate_pass_button.grid(column=2, row=3)
# add
add_button = Button(text="Add", width=44, bg="white", command=save_password)
add_button.grid(column=1, row=4, columnspan=2)
# search
search_button = Button(text="Search", width=14, bg="white", command=search_command)
search_button.grid(column=2, row=1)

window.mainloop()
