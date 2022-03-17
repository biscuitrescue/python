#!/usr/bin/env python3

import os
import subprocess

p1=subprocess.run(['cat', 'output.txt'], capture_output=True, text=True)
p2=subprocess.run(['grep', '-i' , 'Download', 'output.txt'], capture_output=True, text=True, input=p1.stdout)
print(p2.stdout)

with open('log.py', 'r') as r:
    with open('file.txt', 'w') as f:
        for i in r:
            f.write(i)
