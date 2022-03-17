#!/usr/bin/env python3
l=[1,3,3,2,1,2,5]
for i in l:
    if l.count(i) > 1:
        l.remove(i)
print(l)

