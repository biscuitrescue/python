#!/usr/bin/env python3

import mysql.connector as con
from tkinter import *

obj = con.connect(
    user='root',
    password='Pantera@101',
    host='localhost',
    database="PROJECT"
)

cur1 = obj.cursor()

def check_username():
    pass


root = Tk()

root.title("User Store")
root.geometry("1200x800")
root.configure(background="#292d3e")

username = Entry(
    root,
    bg="#bfbfbf",
    fg="#000000"
)
username.insert(1, "Username")

username.place(
    height=40, width=250,
    y=380, x=475
)

root.mainloop()
