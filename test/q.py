#!/usr/bin/env python3

with open("text.txt") as f:
    lines=f.read()

line = lines.replace(" ", "#")

line = line[:-2]
print(line)
