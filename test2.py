#!/usr/bin/env python3

l=eval(input("Please enter list: "))
d=dict.fromkeys(l)
l=list(d.keys())

print('List without repetitions: ',l)

l1=l[-1:]+l[:-1]
print('New list is: ', l1)
