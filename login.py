from tkinter import *
from tkinter import messagebox
window = Tk()
window.title("Username and Password")
window.geometry("500x500")
window.config(bg="grey")


def login():
    usernames = ["gideon", "naruto", "sasuke", "ichigo", "zenitsu", "rengoku", "tanjiro", "luffy"]
    passwords = ["1000", "2000", "3000", "4000", "5000", "6000", "7000", "8000"]
    found = False
    for x in range(len(usernames)):
        if input_username.get() == usernames[x] and input_password.get() == passwords[x]:
            found = True
            if found:
                messagebox.showinfo("Access granted", "Access granted")
                window.destroy()
                import nextscreen
            else:
                messagebox.showerror("Access denied", "Access denied")


def clear(self):
    input_username.delete(0, END)
    input_password.delete(0, END)


def exit(self):
    window.destroy()


# Labels
username_label = Label(window, text="USERNAME : ")
password_label = Label(window, text="PASSWORD : ")
username_label.place(x=20, y=200)
password_label.place(x=20, y=300)
# Entries
input_username = Entry(window, )
input_password = Entry(window, show="*")
input_username.place(x=100, y=200)
input_password.place(x=100, y=300)
# buttons
login_button = Button(window, text="LOGIN", command=login)
clear_button = Button(window, text="ClEAR", command=clear)
exit_button = Button(window, text="Exit", command=exit)
login_button.place(x=100, y=400)
clear_button.place(x=200, y=400)
exit_button.place(x=300, y=400)


window.mainloop()
