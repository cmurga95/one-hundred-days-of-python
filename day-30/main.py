from tkinter import *
import csv
from tkinter import messagebox
import random
import pandas as pd
import json
import os 
# import pyperclip
# --------------- Search and error handling --------------- #
def search():
    search_value = search_entry.get()
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showerror(message = "Couldn't open file, check path.")
    else:
        if search_value in data:
            email = data[search_value]['email']
            password = data[search_value]['password']
            messagebox.showinfo(title = search_value,
                                message=f"email: {email}\n"
                                        f"password: {password}")
        else:
            messagebox.showinfo(title = "Error", message = f"No details for {search_value} exists.") 
        # raise TypeError("I made this up")
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_gen():
    '''
    This function generates a random password 
    It takes no arguments and outputs the randomly generated password
    '''
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
    x_json = {
        website:{
            "email": email,
            "password": password
        }
    }
    file = "data.json"
    if len(website) == 0 or len(password) == 0 or len(email) == 0:
        messagebox.showwarning(title = "oops", message = "Don't leave empty fields")
    
    else :
        is_ok = messagebox.askokcancel(title = website, message=f"email: {email}"
                                                        f"\nPassword: {password}" 
                                                        "\nOk to save?")
        if is_ok:
            #if file doesnt exists
            if not os.path.exists(file):
                #create a new file
                with open(file, "w") as json_file:
                    json.dump(x_json, json_file, indent = 4)

            #if file exists
            elif os.path.exists(file):
                #open it in read mode 
                with open(file, "r") as json_file:
                #load the data to d
                    d = json.load(json_file)
                    #and update the old data with new data
                    d.update(x_json)
                with open(file, "w") as json_file:
                    #dump the new data to the file
                    json.dump(d, json_file, indent = 4)

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
#search label 
label_search = Label(text = "Search:")
label_search.grid(row = 1, column = 0)
#website label
label_website = Label(text = "Website:")
label_website.grid(row = 2, column = 0)

#email/username label
email_label = Label(text = "Email/Username:")
email_label.grid(row = 3, column = 0)

#password label
password_label = Label(text = "Password:")
password_label.grid(row = 4, column = 0)

# -- Entry -- #
#search 
search_entry = Entry(width = 66)
search_entry.grid(row = 1, column = 1)
search_entry.focus()
#website
website_entry = Entry(width = 66)
website_entry.grid(row = 2, column = 1, columnspan = 2)
#email
email_entry = Entry(width = 66)
email_entry.grid(row = 3, column = 1, columnspan = 2)
email_entry.insert(0, "murga.carlos2013@gmail.com")
#password
password_entry = Entry(width = 46)
password_entry.grid(row = 4, column = 1)

# -- Buttons -- #
#search 
search_button = Button(text = "Search",
                       command = search)
search_button.grid(row = 1, column = 2)
#generate password
generate_password = Button(text = "Generate Password", 
                           command = password_gen)
generate_password.grid(row = 3, column = 2)
#add password

add = Button(text = "add",
             width = 47,
             command = save_data)
add.grid(row = 5, column = 1, columnspan = 2)

window.mainloop()
