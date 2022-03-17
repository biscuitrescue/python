#!/usr/bin/env python3

unit=int(input("Please enter units of electricity consumed: "))

if unit<=50:
    rate=unit*3
    print("$",rate,sep='')
elif unit<=150:
    rate=(50*3) + (unit-50)*4.5 + 50
    print("$",rate,sep='')
elif unit<=250:
    rate=(50*3) + (100*4.5) + (unit-150)*5 + 50
    print("$",rate,sep='')
elif unit>250:
    rate=(50*3) + (100*4.5) + (100*5) + (unit-250)*6.5 + 50
    print("$",rate,sep='')
