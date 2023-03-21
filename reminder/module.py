from tkinter import *
from time import sleep
import csv
from datetime import datetime

status_file = 'status.csv'


def add_entry(entry):
    date = datetime.now().strftime('%d %b %Y')
    day = datetime.now().strftime('%A')
    with open(status_file,'a',newline='') as f:
        wobj = csv.writer(f)
        wobj.writerow([date,day,entry])


def update_entry(entry):
    with open(status_file) as f:
        robj = csv.reader(f)
        L = []
        for i in robj:
            L.append(i)
    for i in range(len(L)):
        if L[i][2]==entry:
            L[i][2]='#$#'+L[i][2]
    with open(status_file,'w',newline='') as f:
        wobj = csv.writer(f)
        wobj.writerows(L)

def lister():
    with open(status_file) as f:
        robj = csv.reader(f)
        L = []
        for i in robj:
            L.append(i)
    return L

