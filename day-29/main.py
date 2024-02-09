from tkinter import *
import csv
from tkinter import messagebox
import random
# import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_gen():

    random.seed(random.randint(1,10000))

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
            'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    symbols = ['!','#','$','%','&','(',')','*','+']
    n_letters = random.randint(10,14)
    n_numbers = round(n_letters/2)
    n_symbols = round(n_letters/3)

    l = random.sample(letters, n_letters)
    n = random.sample(numbers, n_numbers)
    s = random.sample(symbols, n_symbols)
    pasword = l+n+s
    password = random.sample(pasword, len(pasword))

    password = ''.join(password)
    password_entry.insert(0, password)
    # return password
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0 or len(email) == 0:
        messagebox.showwarning(title = "oops", message = "Don't leave empty fields")
    
    else :
        is_ok = messagebox.askokcancel(title = website, message=f"email: {email}"
                                                        f"\nPassword: {password}" 
                                                        "\nOk to save?")
        if is_ok:
            with open("temp.csv", mode = "a", newline = "") as csv_file:
                csv_writer = csv.writer(csv_file)
                csv_writer.writerow([website, email, password])
                website_entry.delete(0, END)
                password_entry.delete(0, END)
                messagebox.showinfo(message="Data saved")
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")

canvas = Canvas(width = 200, 
                height = 200)

logo_image = PhotoImage(file = "logo.png")
canvas.create_image(100,100, image = logo_image)
canvas.grid(row = 0, column = 1, 
            padx = (20), pady = (20))

# -- Labels -- #
#website label
label_website = Label(text = "Website:")
label_website.grid(row = 1, column = 0)

#email/username label
email_label = Label(text = "Email/Username:")
email_label.grid(row = 2, column = 0)

#password label
password_label = Label(text = "Password:")
password_label.grid(row = 3, column = 0)

# -- Entry -- #
#website
website_entry = Entry(width = 66)
website_entry.grid(row = 1, column = 1, columnspan = 2)
website_entry.focus()
#email
email_entry = Entry(width = 66)
email_entry.grid(row = 2, column = 1, columnspan = 2)
email_entry.insert(0, "murga.carlos2013@gmail.com")
#password
password_entry = Entry(width = 46)
password_entry.grid(row = 3, column = 1)

# -- Buttons -- #
#generate password
generate_password = Button(text = "Generate Password", 
                           command = password_gen)
generate_password.grid(row = 3, column = 2)
#add password

add = Button(text = "add",
             width = 47,
             command = save_data)
add.grid(row = 4, column = 1, columnspan = 2)

window.mainloop()
