#!/usr/bin/env python3


l=eval(input("Input list: "))

for i in range(0,len(l),2):
    l[i],l[i+1]=l[i+1],l[i]
print(l)

x=int(len(l)/2)
l=l[x:]+l[:x]
print(l)

print(l[::-1])
