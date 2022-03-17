#!/usr/bin/env python3

print("Enter Shape", "1) Cube", "2) Cuboid", "3) Sphere", sep="\n")

a=int(input("Shape: "))

if a==1:
    l=int(input("Enter length: "))
    print("Volume: ")
    print(l**3, "units")
elif a==2:
    l=int(input("Please enter length: "))
    b=int(input("Please enter width: "))
    h=int(input("Please enter height: "))
    print("Volume: ")
    print(l*b*h, "units")
elif a==3:
    pi=3.14159
    r=float(input("Please enter radius: "))
    print("Volume: ")
    print(4/3*pi*(r**3), "units")
else:
    print("Error")
