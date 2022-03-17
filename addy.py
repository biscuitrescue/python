#!/usr/bin/env python3
from tkinter import *

root = Tk()


def click(a):

    global E1
    global L
    E1.delete(0,END)
    E1.insert(0,L[a])


file=open("hehehe.txt")
L=file.readlines()
file.close()
for i in range(len(L)):
    L[i]=L[i].strip()

# k=1
x_B,y_B=20,20
L2=[]
for i in range(len(L)):
    L2.append(Button(root,text=L[i],command=lambda: click(i)))

# print(L2)
for j in range(len(L2)):
    L2[j].place(x=x_B,y=y_B,width=50,height=30)
    y_B+=40

E1=Entry(root,)
E1.place(x=80,y=20,height=30,width=100)


root.mainloop()
