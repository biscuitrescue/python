#!/usr/bin/env python3

from tkinter import *
import os
from PIL import ImageTk, Image
from time import sleep

directory="/home/trogdor/Pictures/test/"
fontis=("arial", 12)
colour=[
    '#F28FAD', # Colour 0
    '#ABE9B3', # Colour 1
    '#FAE3B0', # Colour 2
    '#96CDFB', # Colour 3
    '#F5C2E7', # Colour 4
    '#89DCEB', # Colour 5
    '#1e1e2e'  # Colour 6
]

root=Tk()
root.title("Happy 23 months :)")
root.configure(background=colour[6])
root.geometry("1000x600")

### Image

x=os.listdir(directory)                                     ### NEEDA SEE ABOUT CYCLING PHOTOS
new=x[i]
canvas=Canvas(root, bg=colour[6])
canvas.place(x=160, y=100, width=680, height=400)
image=ImageTk.PhotoImage(Image.open(directory+new))
canvas.create_image(0, 0, anchor=NW, image=image)

### Functions

def click(a):
    if a==1:
        print("muah")
    elif a==2:
        print("muah muah")

### Buttons

button1=Button(root, text="Prev", command=lambda:click(1), bg=colour[0], font=fontis)
button2=Button(root, text="Next", command=lambda:click(2), bg=colour[0], font=fontis)

# entry1=Entry(root, bg=colour[3], font=fontis)
# entry1.insert(0, "")

### Placement

button1.place(x=50, y=100, width=60, height=400)
button2.place(x=890, y=100, width=60, height=400)

# entry1.place(x=50,y=50, width=200, height=30)

root.mainloop()
