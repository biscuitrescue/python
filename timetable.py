#!/usr/bin/env python3

from calendar import day_name
# from datetime import datetime


days = list(day_name)


class Day:
    def __init__(self, day):
        self.day = day
        self.id = days.index(self.day)


today = Day()


# x=datetime.datetime.today().weekday()
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

class Day:
    def __init__(self, index):
        self.index = index
