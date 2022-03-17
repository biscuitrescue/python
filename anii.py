#!/usr/bin/env python3

import subprocess
import os
from tkinter import *
from PIL import ImageTk,Image
import random

root=Tk()
root.title("Happy Anniversary :)")
root.configure(background="#282a36")
root.geometry("1200x700")

dir2="/home/trogdor/.photos/"
if os.path.exists(dir2):
    pass
else:
    os.mkdir(dir2)

dire="/home/trogdor/Pictures/Wallpapers/"
x=os.listdir(dire)
l=[]
for i in x:
    cmd="convert "+dire+i+" -resize 800x450 "+dir2+i
    subprocess.run(cmd, shell=True)
    img=Image.open(dir2+i)
    image=ImageTk.PhotoImage(img)
    l.append(image)

random.shuffle(l)
i=0
canvas=Canvas(root, width=800, height=450, bg="#282a36")
canvas.create_image(0, 0, anchor=NW, image=l[i])

def click(a):
    global i
    if a==1:
        if i!=0:
            i-=1
            canvas.create_image(0, 0, anchor=NW, image=l[i])

    elif a==2:
        if i!=-1:
            i+=1
            canvas.create_image(0, 0, anchor=NW, image=l[i])
        else:
            random.shuffle(l)
            i=0

b1=Button(root,bg="#aaeedd", fg="#000000", font=("space mono for powerline", 16), command=lambda:click(1), text="\uE0b2")
b2=Button(root,bg="#aaeedd", fg="#000000", font=("space mono for powerline", 16), command=lambda:click(2), text="\uE0b0")

b1.place(x=55, y=50, width=80, height=600)
b2.place(x=1060, y=50, width=80, height=600)
canvas.place(x=200,y=125,height=450,width=800)

root.mainloop()
