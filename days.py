#!/usr/bin/env python3

day=input("Enter the day: ")

if day=="MONDAY" or day=="Monday" or day=="monday":
    na=1
if day=="TUESDAY" or day=="Tuesday" or day=="tuesday":
    na=2
if day=="WEDNESDAY" or day=="Wednesday" or day=="wednesday":
    na=3
if day=="THURSDAY" or day=="Thursday" or day=="thursday":
    na=4
if day=="FRIDAY" or day=="Friday" or day=="friday":
    na=5
if day=="SATURDAY" or day=="Saturday" or day=="saturday":
    na=6
if day=="SUNDAY" or day=="Sunday" or day=="sunday":
    na=7
else:
    print("Invalid day","Please check spelling","Program is case-sensitive",sep="\n")

no=int(input("Number of days to add: "))
f=no%7+na

if f==1:
    print("Monday")
if f==2:
    print("Tuesday")
if f==3:
    print("Wednesday")
if f==4:
    print("Thursday")
if f==5:
    print("Friday")
if f==6:
    print("Saturday")
if f==7:
    print("Sunday")
