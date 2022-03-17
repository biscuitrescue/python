#!/usr/bin/env python3

str1="HELU (i ()am here) {or am i} [ ][ 2323"
match=[
    ['(','{','['],
    [')','}',']'],
]
check={}
for i in range(3):
    check.update(
        {
            match[0][i]:match[1][i]
        }
    )
print(check)
str2=''
for i in str1:
    if i.isalnum() or i.isspace():
        pass
    else:
        str2+=i
# print(str2)
