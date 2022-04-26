#!/usr/bin/env python3

class Computer:

    def __init__(self, *args):
        self.cpu = args[0]
        self.mem = args[1]

    def config(self):
        print(self.cpu, self.mem)


a = 9
com1 = Computer("i5", 15)
com2 = Computer("ryzen5", 16)

com2.config()
com1.config()

Computer.config(com1)
Computer.config(com2)
