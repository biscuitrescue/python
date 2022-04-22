#!/usr/bin/env python3

from tkinter import *

### Argyments

widget=dict(
    fg=colours["fg"],
    bg=colours["cyan"],
)

placed=dict(
    width=100,
    height=50,
)

### Colours

colours={
    "red":"#ff5555",
    "blue":"#9cc4ff",
    "black":"#000000",
    "bg":"#292d3e",
    "fg":"#dfdfdf",
    "cyan":"#aaeedd"
}

root=Tk()
root.configure(background="#292d3e")
root.geometry("1000x700")
root.title("Testing ...")


entry=Entry(
    root,
    **widget,
)

entry.place(
    **placed
)

root.mainloop()