#!/usr/bin/env python3

def myMean(l):
    l1=[]
    summ=0
    for i in l:
        if type(i)==float:
            l1.append(i)
    for i in range(len(l1)):
        summ+=l1[i]
    print(summ/3)
llist=[1,22,2,1.2,1.4,1.22]
myMean(llist)

def calcFact(x):
    fac=1
    for i in range(x,0,-1):
        fac*=i
    print(fac)

x=int(input("enter number: "))
calcFact(x)

