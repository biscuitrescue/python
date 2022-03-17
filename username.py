#!/usr/bin/env python3

from tkinter import *
# from tkinter.ttk import *

root=Tk()
root.title("User Store")
root.configure(background="#2e3440")

e=Entry(root, width=30, bg='#aaeedd', fg='#000000')
e.grid(row=0,column=0,columnspan=2, ipadx=20, ipady=5)
e.insert(0,'Enter username')

d={}

### FUNCTIONS ###

def myClick1():
    y=r.get()
    u='!@#$%^&*()_-+=";:'
    li=0
    lc=0
    lu=0
    ll=len(str(y))
    for i in range(ll):
        if y[i].isdigit():
            li+=1
        elif y[i] in u:
            lc+=1
        elif y[i].isupper():
            lu+=1
    global ex
    if li==0:
        ex=Entry(root, width=30, bg='#292a36', fg='#f3f4f5')
        ex.grid(row=3,column=0, ipadx=20, ipady=5)
        ex.insert(0, 'Password requires atleast one number!')
    else:
        ex=Entry(root, width=30, bg='#2e3440', fg='#f3f4f5')
        ex.grid(row=3,column=0, ipadx=20, ipady=5)
        ex.destroy()
    if lc==0:
        ex=Entry(root, width=30, bg='#292a36', fg='#f3f4f5')
        ex.grid(row=3,column=0, ipadx=20, ipady=5)
        ex.insert(0, 'Password requires atleast special character!')
    else:
        ex=Entry(root, width=30, bg='#2e3440', fg='#f3f4f5')
        ex.grid(row=3,column=0, ipadx=20, ipady=5)
        ex.destroy()
    if lu==0:
        ex=Entry(root, width=30, bg='#292a36', fg='#f3f4f5')
        ex.grid(row=3,column=0, ipadx=20, ipady=5)
        ex.insert(0, 'Password requires atleast capital letter!')
    else:
        ex=Entry(root, width=30, bg='#2e3440', fg='#f3f4f5')
        ex.grid(row=3,column=0, ipadx=20, ipady=5)
        ex.destroy()
    if ll<10:
        ex=Entry(root, width=30, bg='#292a36', fg='#f3f4f5')
        ex.grid(row=3,column=0, ipadx=20, ipady=5)
        ex.insert(0, 'Password requires atleast 10 characters!')
    else:
        ex=Entry(root, width=30, bg='#2e3440', fg='#f3f4f5')
        ex.grid(row=3,column=0, ipadx=20, ipady=5)
        ex.destroy()
    if li>0 and lc>0 and lu>0 and ll>=10:
        global d
        d.update({x:y})
        global user
        user=d.keys()
        global pas
        pas=d.values()
        global button2
        button2=Button(root, text="Show users", command=myClick2, bg='#aec597', fg='#000000')
        button2.grid(row=3, column=3, ipadx=20, ipady=5)
        ex=Entry(root, width=30, bg='#2e3440', fg='#f3f4f5')
        ex.grid(row=3,column=0, ipadx=20, ipady=5)
        button1.destroy()

def myClickx():
    global x
    x=str(e.get())
    while x in d:
        ey=Entry(root, bg='#FF7696', fg='#000000')
        ey.grid(row=3, column=2, ipadx=15, ipady=5)
        ey.insert(0, 'Username not unique!')
        break
    while x not in d:

        ey=Entry(root, bg='#2e3440', fg='#000000')
        ey.grid(row=3, column=2, ipadx=15, ipady=5)
        global button1
        button1=Button(root, text="Add user", command=myClick1, bg='#aec597', fg='#000000')
        button1.grid(row=0, column=3, ipadx=20, ipady=5)
        global r
        r=Entry(root, width=30, bg='#aaeedd', fg='#000000')
        r.grid(row=1,column=0,columnspan=2, ipadx=20, ipady=5)
        break

def myClick2():
    for i in d:
        e2=Entry(root, width=30, bg='#2e3440', fg='#f3f4f5')
        e2.insert(0,i+' : '+d[i])
        for i in range(len(d.keys())):
            e2.grid(row=5+i, column=3, ipadx=20, ipady=5)
        button2.destroy()

buttonx=Button(root, text="Check username", command=myClickx, bg='#aec597', fg='#000000')
buttonx.grid(row=0, column=2, ipadx=18, ipady=5)

root.mainloop()
