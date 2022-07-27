#!/usr/bin/env python3

import mysql.connector as con
from tkinter import *

obj = con.connect(
    user='root',
    password='Pantera@101',
    host='localhost',
    database="PROJECT"
)

class Window(Tk):
    def __init__(self):
        Frame.__init__(main, self)


cur1 = obj.cursor()


root = Tk()

root.title("User Store")
root.geometry("1200x800")
root.configure(background="#1e1e2e")

main_frame = Frame(
    root,
    bg="#1e1e2e",
)
main_frame.place(
    width=1200, height=800
)

root.mainloop()
