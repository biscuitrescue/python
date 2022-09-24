#!/usr/bin/env python3

import csv

# user = input("Enter username: ")
# password = input("Enter Password: ")

# with open("hehe.csv", "w+") as f:
#     wobj = csv.writer(f)
#     wobj.writerow([user, password])

with open("hehe.csv") as f:
    obj = csv.reader(f)
    for record in obj:
        print(record)

# Read a text file and display the number of vowels/consonants/uppercase/lowercase characters in the file

# count = 0

# with open("hehe.txt") as f:
#     x = f.read()
#     for i in x:
#         if i in "aeiou":
#             count += 1

# print(count)

# Remove all the lines that contain the character a’ in a file and write it to another file

# with open("hehe.txt") as f:
#     added = []
#     x = f.readlines()
#     print(len(x))
#     for i in x:
#         if 'a' in i:
#             added.append(i)
#             x.remove(i)

# with open("hehe.txt", "w") as f:
#     f.writelines(x)

# with open("added.txt", "w") as f:
#     f.writelines(added)
