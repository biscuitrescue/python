#!/usr/bin/env python3

name=('add','kart','tan','deep')
nomb=[12,43,22,66]

d=dict.fromkeys(nomb)
l=list(d)

for i in range(len(l)):
    d[l[i]]=list(name)[i]

n=int(input("Please enter number: "))
if n in d:
    d.pop(n)
    print(d)
else:
    print(str(n)+' is not in dictionary')
