#!/usr/bin/env python3

### Bubble sort
l=[4,5,3,2,1,6,7,3,9]
l2=list(l)
for j in range(len(l)):
    for i in range(len(l)-1):
        if l[i]>l[i+1]:
            l[i],l[i+1]=l[i+1],l[i]
print(l)

### Selection sort
for i in range(len(l2)):
    for j in range(i+1,len(l2)):
        if l2[i]>l2[j]:
            l2[i],l2[j]=l2[j],l2[i]
print(l2)
