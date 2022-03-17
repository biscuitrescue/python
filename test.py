#!/usr/bin/env python3

N=int(input("Enter number of names: "))

d={}

for i in range(N):
    x=input("Enter your name: ")
    y=input("Enter your phone number: ")
    d.update({x:y})

print()
tek=input("Enter name for number: ")
print(d[tek])

n=[]
n1=[]
d2={}
l=list(d.keys())
l2=list(d.values())
for i in l:
    if l2.count(d[i])==1:
        n.append(i)
        n1.append(d[i])
d2=dict(zip(n,n1))
print(d2)
