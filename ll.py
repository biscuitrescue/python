#!/usr/bin/env python3

Data=list("Do It @ 123 !")
d={}

for i in range(len(Data)-1):
    if (Data[i].isupper()):
        d.update({Data[i]:Data[i].lower()})
    elif (Data[i].isspace()):
        d.update({Data[i]:Data[i+1]})

print(d)
