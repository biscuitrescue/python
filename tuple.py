#!/usr/bin/env python3

from num2words import num2words

l1=[1,2,3,4,5,6,7,8]
l2=[]
for i in l1:
    x=num2words(i)
    l2.append(x)
d=dict.fromkeys(l1)
for k in range(len(d)):
    d.update({l1[k]:l2[k]})
    # d[l1[k]]=l2[k]
print(d)
