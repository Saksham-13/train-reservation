from operator import indexOf
from tkinter import *
import json

with open("user.json") as file:
    f = json.load(file)

username_login_entry,password__login_entry = 0,0
def close_window():
    global username_login_entry,password__login_entry
    flag = False
    us = username_login_entry.get()
    pw = password__login_entry.get()
    if( us in f["username"]):
        a = f["username"].index(us)
        if( pw == f["password"][a]):
            flag = True
        
    
    if (flag):
        print("yes")
        login_screen.destroy()
        import destination
        destination.main()

    else:
        LoginPage()


login_screen=Tk()

def LoginPage():
    global username_login_entry,password__login_entry
    
    login_screen.title("Login")
    login_screen.geometry("700x250")
    Label(login_screen, text="Please enter correct login details").pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Username").pack()
    username_login_entry = Entry(login_screen, textvariable="username")
    username_login_entry.pack()
    
    Label(login_screen, text="").pack()
    Label(login_screen, text="Password").pack()
    password__login_entry = Entry(login_screen, textvariable="password", show= '*')
    password__login_entry.pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Login",command = close_window, width=10, height=1).pack()
    login_screen.mainloop()
LoginPage()