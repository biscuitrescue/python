#!/usr/bin/env python3
from tkinter import *

count = 0

def change(yes):
    global count
    if yes:
        yesframe.tkraise()
    else:
        if count <= 2:
            frame.place_forget()
            frame.place(height="200", width="600")
            count += 1
        else:
            count = 0
            noframe.tkraise()

def takemeback():
    frame.tkraise()

root = Tk()
root.configure(background="white")
root.geometry("600x200")

main = Frame(root, bg='white')
main.place(height="200", width="600")


yesframe = Frame(root, bg='white')
yesframe.place(height="200", width="600")


noframe = Frame(root, bg='white')
nolabel = Label(
    noframe,
    text="Are you sure about that?",
    bg="white",
    fg="black"
)
nolabel.pack(expand=True)

back_button = Button(
    noframe,
    text="No",
    bg="white",
    fg="black",
    command=takemeback
)

back_button.place(x="480", y="150")

noframe.place(height="200", width="600")

label = Label(
    main,
    text="You have been hacked.\nPlease comply with the following",
    bg="white",
    fg="black"
)
label.pack(expand=True)

okay = Button(
    main,
    text="Okay",
    bg="white",
    fg="black",
    command=lambda: frame.tkraise()
)
okay.place(x=450, y=150)

frame = Frame(root, bg="white")
frame.place(height="200", width="600")

yes = Button(
    frame,
    text="Yes",
    bg="white",
    fg="black",
    command=lambda: change(True)
)
yes.place(x="400", y="150")

no = Button(
    frame,
    text="No",
    bg="white",
    fg="black",
    command=lambda: change(False)
)
no.place(x="480", y="150")

label = Label(
    frame,
    text='Be my valentine',
    bg="white",
    fg="black"
)
label.pack(expand=True)
main.tkraise()

root.mainloop()
