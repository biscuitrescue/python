#!/usr/bin/env python3

from tkinter import *

colours={
    "red":"#ff5555",
    "black":"#000000",
    "bg":"#292d3e",
    "blue":"#9cc4ff",
    "fg":"#dfdfdf",
    "cyan":"#aaeedd"
}

fg=colours["black"]

root=Tk()

widget=dict(
    fg=colours["black"],
    bg=colours["cyan"]
)

root.configure(background=colours["bg"])
root.geometry("1000x700")
root.title("Testing ...")

entry=Entry(
    **widget,
)

entry.place(
    x=40,
    y=40,
    width=100,
    height=50,
)

root.mainloop()
