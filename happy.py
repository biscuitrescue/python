#!/usr/bin/env python3

a=int(input("Please enter number: "))

if a>=100 and a<=999:
    x=a//100
    y=(a%100)//10
    z=a%10
    if (x**2)+(y**2)+(z**2)==1:
        print("The number is a happy number")
    else: print("The number is not a happy number")
else: print("the number is not 3 digit")
