#!/usr/bin/env python3
import subprocess
import random
from tkinter import *
import os
from time import sleep

L = range(0,100)

username = input("Username: ")
if os.path.exists(username+".txt"):
    exister = True

    
else:
    print("Account does not exist")
    exit()


while True:
    file = open(username+".txt")
    print("Your balance is: ",end='')
    balance = int(file.read())
    print(balance)
    if balance == 0:
        print("You do not have money to play")
        break
    L2 = random.sample(L,5)
    print("Possible outcomes are:")
    print(L2)
    print()
    while True:
        bid = int(input("Place your bid: "))
        if bid<=balance:
            break
        else:
            print("You do not have enough money")
            continue

    print()

    guess = int(input("Place your guess: "))
    print()
    x = random.choice(L2)
    sleep(3)
    print("Outcome is",x)
    if x == guess:
        print()
        print("Correct guess")
        balance+=3*bid
        print("You have gained",3*bid,"coins.")
        file.close()
        file = open(username+".txt",'w')
        file.write(str(balance))
        file.close()

    else:
        print()
        print("Your guess was incorrect")
        balance-=bid
        print("You have lost",bid,"coins.")
        file.close()
        file = open(username+".txt",'w')
        file.write(str(balance))
        file.close()
    again = input("Another round or quit? [1,2]: ")
    if again == "1":
        continue
    elif again == "2":
        break


print("Your final balance is",balance)
print()
print("Thankyou for playing")
exit()
