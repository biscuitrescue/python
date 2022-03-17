#!/usr/bin/env python3
from tkinter import *
import os
from datetime import date

root = Tk()
root.title("To-do list")
root.configure(background="#282a36")
root.geometry("700x400")

fontboi="Calibri"
tt_file = "/home/karttikeya/.do.txt"

if os.path.exists(tt_file):
    None
else:
    file = open(tt_file,'w')
    file.close()

file = open(tt_file)
Lis1 = file.readlines()
file.close()

def printer():
    global L1
    global Lis1
    global s
    s = '\n  To do list:\n'
    for i in range(len(Lis1)):
        s+="    "+str(i+1)+") "+Lis1[i]
    L1 = Label(root,text=s,bg="#f1fa8c",justify="left",anchor="nw", font=(fontboi,13))
    L1.place(x=350,y=0,height=4000,width=4000) 

printer()

def click1(a):
    global s
    global E1
    global Lis1
    work = E1.get()
    if a == 1:
        if work[0]==">":
            index=''
            for i in range(len(work)):
                if work[i].isdigit()==True:
                    index+=work[i]
                elif work[i]==">" or work[i]==")" or work[i]==" ":
                    continue
                else:
                    work = work[i:]
                    break
            Lis1[int(index)-1]=work.title()+'\n'
        else:
            Lis1.append(work.title()+'\n')
    elif a == 2:
        wdone = int(work)
        Lis1.pop(wdone-1)

    elif a == 3:
        wdone = int(work)
        str1=Lis1[wdone-1]
        str2='\u0336'
        for c in str1:
            str2+= c + '\u0336'
        Lis1.pop(wdone-1)
        Lis1.append(str2[:-1])

    printer()
    file = open(tt_file,'w')
    for i in Lis1:
        file.write(i)
    file.close()
    E1.delete(0,END)

E1 = Entry(root,bg="#f1fa8c", font=(fontboi,12))
B1 = Button(root,text="Add/Modify(>) ",command=lambda:click1(1),bg="#8be9fd", font=(fontboi,11),bd=0)
B2 = Button(root,text="Remove",command=lambda:click1(2),bg="#ff5555", font=(fontboi,11),bd=0)
B3 = Button(root,text="Job Done",command=lambda:click1(3),bg="#50fa7b",font=(fontboi,11),bd=0)
L1 = Label(root,text=s,bg="#f1fa8c",justify="left",anchor="nw", font=(fontboi,13))

E1.place(x=25,y=145,height=30,width=300)
B1.place(x=25,y=185,height=30,width=145)
B2.place(x=180,y=185,height=30,width=145)
B3.place(x=25,y=225,height=30,width=300)
L1.place(x=350,y=0,height=4000,width=4000)



root.mainloop()
