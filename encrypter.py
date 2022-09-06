#!/usr/bin/env python3

from cryptography.fernet import Fernet

# key = Fernet.generate_key()

# with open("algo.key", "wb") as f:
#     f.write(key)
with open("algo.key", "rb") as f:
    key = f.read()

fernet = Fernet(key)

with open("hehe.txt") as hehe:
    x = hehe.read()

new = fernet.encrypt(x)

with open("newfile.txt", "wb") as f:
    f.write(new)
