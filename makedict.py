#!/usr/bin/env python3

### Dictionary

dict1={
    "Januray":31,
    "February":28,
    "March":31,
    "April":30,
    "May":31,
    "June":30,
    "July":31,
    "August":31,
    "September":30,
    "October":31,
    "November":30,
    "December":31,
}

for i in dict1:
    if dict1[i]>30:
        print(i)

### Find

xx=int(input("Enter number: "))
xl=eval(input("Enter list of numbers: "))

if xx in xl:
    print("The index is: "xl.index(xx))
else:
    print("The number was not found in list")

### Tuple

t=(1,2,3,4,22,21,1,2)
l=list(t)
l.remove(max(l))
print(max(l))
