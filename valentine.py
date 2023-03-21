#!/usr/bin/env python3


from tkinter import *
from tkinter import messagebox
import random

count = 0

def show_random_compliment():
    compliments = [
        "I never knew i could fall this bad for someone with such mediocre taste in football clubs ;)",
        "Your voice makes me calm down so quick?!?",
        "You make my heart skip a beat. Rok mat dena galti se kabhi",
        "Not to be too political, but you're looking fine as fuckkkkkk",
        "I never really realised how much god liked me until he made you fall for me",
        "You're my angel of small death, I am yours, just yours ;)",
        "I'm so in love that I might stop breathing",
        "Everytime i look at you, its like the first time"
    ]
    messagebox.showinfo("Compliment of the Day", random.choice(compliments))

def change(yes):
    global count
    if yes:
        yesframe.tkraise()
    else:
        if count < 1:
            frame.place_forget()
            frame.place(height="200", width="600")
            count += 1
        else:
            count = 0
            noframe.tkraise()

root = Tk()
root.configure(background="white")
root.geometry("600x200")

main = Frame(root, bg='white')
main.place(height="200", width="600")


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
yesframe = Frame(root, bg='white')
header = Label(
    yesframe,
    text="To my beloved Tanvi,",
    bg="white",
    fg="black"
)
header.pack(expand=True)

valentine_gift = Button(
    yesframe,
    text="Heh",
    command=show_random_compliment,
    bg='white',
    fg='black'
    )
valentine_gift.place(x="400", y="150")

back_button2 = Button(
    yesframe,
    text="No",
    bg="white",
    fg="black",
    command=frame.tkraise
)

back_button2.place(x="480", y="150")


yesframe.place(height="200", width="600")


noframe = Frame(root, bg='white')
nolabel = Label(
    noframe,
    text="Are you sure about that? (No is not an option)",
    bg="white",
    fg="black"
)
nolabel.pack(expand=True)

back_button = Button(
    noframe,
    text="No",
    bg="white",
    fg="black",
    command=frame.tkraise
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

main.tkraise()
root.mainloop()
