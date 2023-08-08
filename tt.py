#!/usr/bin/env python3

from calendar import day_name
from datetime import datetime
from os.path import realpath, exists
from tkinter import *
import pickle


days = list(day_name)

file = realpath(__file__)
file = file[:file.rfind('/')+1]+'tt.txt'

print(file)


class Day:
    def __init__(self, day):
        self.day = day
        self.id = days.index(self.day)

        if exists(file):
            self.content = self.read_from_file()
        else:
            self.content = list()

    def read_from_file(self):
        with open(file, 'rb') as f:
            x = pickle.load(f)
        return x

