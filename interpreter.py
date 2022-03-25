#!/usr/bin/env python3

from multiprocessing import Process
import string
from random import shuffle
from os.path import exists

def get_key():
    keyx=list(string.ascii_letters+string.digits+string.punctuation)
    keyx.remove("\\")
    keyx.remove("'")
    keyx.remove('"')
    keyx.remove(".")
    shuffle(keyx)
    key=""
    for i in keyx:
        key+=i
    with open("key.txt", "w") as f:
        f.write(key)


def make_pass(password: str):
    if exists("key.txt"):
        pass
    else:
        while True:
            x=input("key.txt not found. Do you want to make a new one?\n[y/n] ")
            if x in "Yy":
                response = True
                break
            elif x in "nN":
                response = False
                break
            else:
                "Invalid Response"
        if response:
            get_key()
        else:
            print("Exiting ...")
            exit()

    with open("key.txt", "r") as f:
        key=f.read().strip()

    # s=""
    # for i in password:
    #     encrypt=dict(
    #
    #      )

giv=input("Enter your pass: ")
make_pass(giv)
