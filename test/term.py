#!/usr/bin/env python3

import pickle

def AddOrder():
    with open("Stock.dat", "ab") as f:
        pickle.dump((orderid, medname, quantity, price))

def DisplayPrice():
    with open("Stock.dat", "rb") as f:
        x =  pickle.load(f)
        for i in x:
            if int(i[-1]) > 500:
                print(i)

