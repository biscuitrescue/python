#!/usr/bin/env python3


from customtkinter import *


class Frame(CTkFrame):
    def __init__(self, root):
        super().__init__(root)
        self.configure(fg_color="black")
        self.pack()

root = CTk()
frame = Frame(root)

root.mainloop()
