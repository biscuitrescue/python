#!/usr/bin/env python3
from json import dumps

l=['list','hih','aibohphobia','no']
d={}

for i in l:
    d.setdefault(i)
    # if i==i[::-1]:
    #     d[len(i)]=
print(dumps(d, indent=2))
