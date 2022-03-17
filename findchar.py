#!/usr/bin/env python3

a=input(str("Please enter string: "))
b=input(str("Please input your character: "))

for i in range(0,len(a)):
    if a[i]==b:
        print(i)
