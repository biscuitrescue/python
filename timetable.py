#!/usr/bin/env python3

from calendar import day_name
from datetime import datetime
from os.path import realpath


days = list(day_name)


class Day:
    def __init__(self, day):
        self.day = day
        self.id = days.index(self.day)
        self.content = list()

    def add_single(self, content):
        self.content.append(content)

    def add_multiple(self, content):
        self.content.extend(content)

    def write_to_file(self):
        file = realpath(__file__)
        for i in range(len(file)-1, 0, -1):
            if file[i] == '/':
                file = file[:i+1]
                break

        print(file[0:len(__file__)])

    def del_content(self, content):
        self.content.remove(content)

    def __str__(self):
        return f"{self.day}:\n\t work to be done: {[i for i in self.content]}"


today = Day(datetime.now().strftime("%A"))
today.write_to_file()

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

