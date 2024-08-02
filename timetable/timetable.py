#!/usr/bin/env python3

from calendar import day_name
from datetime import datetime
from os.path import realpath, exists
# from tkinter import *
import pickle


days = list(day_name)

file = realpath(__file__)
file = file[:file.rfind('/')+1]+'content.txt'


class Day:
    def __init__(self, day):
        self.day = day
        self.id = days.index(self.day)
        if exists(file):
            self.content = self.read_from_file()
        else:
            self.content = list()

    def add_single(self, content):
        if content not in self.content:
            self.content.append(content)

    def add_multiple(self, content):
        if not any(i in self.content for i in content):
            self.content.extend(content)

    def read_from_file(self):
        with open(file, 'rb') as f:
            x = pickle.load(f)
        return x

    def write_to_file(self):
        with open(file, 'wb') as f:
            pickle.dump(self.content, f)

    def del_content(self, selected):
        if selected == 'all':
            i = len(self.content)-1
        for i in range(len(self.content)):
            if i in selected:
                del self.content[i]

    def __str__(self):
        return f"{self.day}:\n\t work to be done: {[i for i in self.content]}"


today = Day(datetime.now().strftime("%A"))
today.add_multiple(("hehe", "hi"))
today.del_content('all')

# x+=1
#
# print()
#
# days = {
#
#     1:' Monday\n\tNone',
#     2:' Tuesday\n\t5:30 PM - 7:30 PM | Physics',
#     3:' Wednesday\n\t8:15 PM - 10:15 PM | Chemistry',
#     4:' Thursday\n\t4:00 PM - 6:00 PM | Physics',
#     5:' Friday\n\t8:15 PM - 10:15 PM | Chemistry',
#     6:' Saturday\n\t9:30 AM - 4:00 PM | VMC',
#     7:' Sunday\n\t9:30 AM - 4:00 PM | VMC',
#
# }
#
# for i in range(len(days)):
#     if i==x:
#         print(days[x])
