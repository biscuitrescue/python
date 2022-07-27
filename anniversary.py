#!/usr/bin/env python3

from os import listdir
from os import getcwd
from tkinter import *
from PIL import ImageTk, Image
from random import shuffle

root=Tk()
root.title("Happy Anniversary :)")
root.configure(background="#282a36")
root.geometry("1200x700")

dir2=getcwd()+'/photos/'
x=listdir(dir2)
l=[]
for i in x:
    img=Image.open(dir2+i)
    image=ImageTk.PhotoImage(img)
    l.append(image)

shuffle(l)
i=0
label=Label(root, image=l[i], background="#282a36")
# canvas.create_image(0, 0, anchor=NW, image=l[i])

def click(a):
    global i
    if a==1:
        if i!=0:
            i-=1
            label=Label(root, image=l[i], background="#282a36")
            label.place(x=200,y=50,height=600,width=800)

    elif a==2:
        if i!=len(l)-1:
            i+=1
            label=Label(root, image=l[i], background="#282a36")
            label.place(x=200,y=50,height=600,width=800)
        else:
            shuffle(l)
            i=0

b1=Button(root,bg="#aaeedd", fg="#000000", font=("arial", 16), command=lambda:click(1), text="<")
b2=Button(root,bg="#aaeedd", fg="#000000", font=("arial", 16), command=lambda:click(2), text=">")

b1.place(x=55, y=50, width=80, height=600)
b2.place(x=1060, y=50, width=80, height=600)
label.place(x=200,y=50,height=600,width=800)

root.mainloop()
