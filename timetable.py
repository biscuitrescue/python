#!/usr/bin/env python3

import datetime

x=datetime.datetime.today().weekday()
x=x+1

if x==1:
    day='   Monday:'
    classes='''
        3:30 PM - 5:30 PM | VMC
        6:00 PM - 8:00 PM | VMC
    '''
elif x==2:
    day='   Tuesday:'
    classes='''
        7:00 PM - 9:00 PM | Physics
        7:00 PM - 9:00 PM | Chemistry
    '''
elif x==3:
    day='   Wednesday:'
    classes='''
        3:30 PM - 5:30 PM | VMC
        6:00 PM - 8:00 PM | VMC
    '''
elif x==4:
    day='   Thursday:'
    classes='''
        7:00 PM - 9:00 PM | Physics
        7:00 PM - 9:00 PM | Chemistry
    '''
elif x==5:
    day='   Friday:'
    classes='''
        3:30 PM - 5:30 PM | VMC
        6:00 PM - 8:00 PM | VMC
    '''
elif x==6:
    day='   Saturday:'
    classes='''
        11:30 AM - 1:00 PM | Chemistry
    '''
else:
    day='   Sunday:'
    classes='''
        9:00 AM - 11:00 AM | Physics
    '''

print(day,classes,sep="\n")
