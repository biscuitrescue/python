#!/usr/bin/env python3

from tkinter import *
from subprocess import run

root = Tk()
root.title("Power Menu")
root.geometry("850x250")

# buttons = {
#     "Suspend":"Yellow",
#     "Shutdown":"Red",
#     "Hibernate":"Black",
#     "Lock":"White",
# }

buttons = [
    ###  Fn()    colour   x
    ["Suspend", "yellow", 50],
    ["Shutdown", "red", 250],
    ["Hibernate", "black", 450],
    ["Lock", "white", 650],
]

for i in range(len(buttons)):
    button = Button(
        root,
        background = buttons[i][1],
    )
    button.place(
        x=buttons[i][2], y=50,
        width=150, height=150
    )

# sleep=Button(
#     root,
#     background="yellow",
# )

# sleep.place(
#     x=50, y=50,
#     width=150 , height=150

# )

root.mainloop()
